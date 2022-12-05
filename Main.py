import streamlit as st
#Animation
import json
import requests
from streamlit_lottie import st_lottie
import time

#progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

st.markdown("<h1 style='text-align: center; color: white;'>Activity Detection Web Application</h1>", unsafe_allow_html=True)


#@st cache for animation and loaded data
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ani1 = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_kw5jwkm0.json")
st_lottie(
    lottie_ani1,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)

st.markdown("<h3 style='text-align: left; color: white;'> Motion Detection Web App which Detects various Activities.</h3>", unsafe_allow_html=True)

lottie_ani2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_1jLSEj.json")
st_lottie(
    lottie_ani2,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)

st.markdown("<h3 style='text-align: right; color: white;'> For support contact ayush31598@gmail.com </h3>", unsafe_allow_html=True)