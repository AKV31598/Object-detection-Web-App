import streamlit as st
import cv2
import numpy as np
import time

# progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

# Load Yolo
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")
classes = []
with open("yolo/coco.names", "r") as f: 
  classes = [line.strip() for line in f.readlines()] 
output_layers = net.getUnconnectedOutLayersNames()  

colors = np.random.uniform(0, 255, size=(len(classes), 3))

st.markdown("<h1 style='text-align: center; color: white;'>Camera Live Feed (Object Detection) </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'> This is Basic Implementation of Object Detection. </h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'> As you can see the output shown in camera frame, the objects are detected and a rectangular shapes appears around the object. </h4>", unsafe_allow_html=True)

run = st.checkbox('Run', value=True)
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)
# height, width, channels = cap.shape

while run:
    _, frame = cap.read()
    print(frame)

    up_points = (1000,700)
    frame = cv2.resize(frame, up_points, fx=2.0, fy=1.9)
    height, width, channels = frame.shape
    
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)  
    outs = net.forward(output_layers)
    # height = FRAME_WINDOW.height
    # width = FRAME_WINDOW.width

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.9: #chng
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
            cv2.putText(frame, label, (x, y + 30), font, 3, color, 2)



    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
