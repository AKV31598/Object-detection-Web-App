import streamlit as st
import cv2
# from playsound import playsound
import time

# progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)
body_classifire=cv2.CascadeClassifier("yolo\haarcascade_fullbody.xml")


st.title("Webcam Live Feed")
run = st.checkbox('Run', value=True)
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()

    # ret_, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=body_classifire.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        cv2.putText(gray, "Intrusion Detected", (210, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
