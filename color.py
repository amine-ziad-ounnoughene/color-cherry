
from colormap import rgb2hex,hex2rgb
import numpy as np
from PIL import Image
import streamlit as st
#import streamlit as st
st.title("color cherry")
st.write("this app tries to show you the most frequents pixel values in your image ")
most = st.number_input('Insert the number of the most frequent pixels you wanna show : ',value=3,step=1)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png"])

def colors(x,most_frequent=5):
  X = x
  colors, inv = np.unique(X.reshape(-1, 3), axis=0, return_inverse=True)
  inv.reshape(X.shape[:2])
  for i in range(1,most_frequent+1):
    a = np.bincount(inv).argsort()[-i]
    c = colors[a][0],colors[a][1],colors[a][2]
    k = []
    h = []
    for iy in range(1,20):
       k.append([c])
    for ih in range(1,20):
       h.append(k)
    st.image(np.array(h).reshape([19,19,3]))
    st.write("hex : "+ str(rgb2hex(colors[a][0],colors[a][1],colors[a][2])))
    st.write("RGB : " + str(hex2rgb(rgb2hex(colors[a][0],colors[a][1],colors[a][2]))))
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.asarray(image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    colors(image,most_frequent=most)
    
    st.balloons()
