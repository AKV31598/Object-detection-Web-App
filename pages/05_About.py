import streamlit as st 
import time

#progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

st.markdown("<h1 style='text-align: center; color: white;'> ABOUT US </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'> ACTIVITY DETECTION WEB APP </h4>", unsafe_allow_html=True)

#@st cache for animation and loaded data
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



#Animation
import json
import requests
from streamlit_lottie import st_lottie
lottie_ani1 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ljotbiif.json")

st_lottie(
    lottie_ani1,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)


st.markdown("<h4 style='text-align: center; color: white;'>Human activity recognition or HAR is the process of interpreting human motion using computer and machine vision technology. Human motion can be interpreted as activities, gestures, or behaviors which are recorded by sensors mainly Camaras.</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>The movement data is then translated into action commands for computers to execute and analyze human activity recognition code </h4>", unsafe_allow_html=True)



#@st cache for animation and loaded data
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Animation
import json
import requests
from streamlit_lottie import st_lottie
lottie_ani2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ybyrkqbg.json")

st_lottie(
    lottie_ani2,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)

st.markdown("<h1 style='text-align: center; color: white;'>This project has been done by</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left; color: white;'>Ayush Kumar Vishwakarma, Ujwal Pravin Patil</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left; color: white;'>Atharva Narendra Rao, Yash Nashik Bante</h4>", unsafe_allow_html=True)
