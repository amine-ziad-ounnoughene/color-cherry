
from colormap import rgb2hex,hex2rgb
import numpy as np
from PIL import Image
import streamlit as st
#import streamlit as st
st.title("color cherry")
st.write("are you a graphic designer and you usually struggle to know the pixel value of the most frequent values in your image **color cherry** is here for you and for **free** ")
most = st.number_input('Insert the number of the most frequent pixels you wanna show : ',value=3,step=1)
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
colors_dict = {'Black' : "#000000",
"Gray" : "#CCCCCC",
"White" : "#FFFFFF",
"Red" : "#FF0000",
"Blue" : "#0000FF",
'Green' : "#008000",
'Yellow' : "#FFFF00",
 "Orange" : "#FFA500",
 "Violet" : "#800080"}
inversed_color = {value : key for (key, value) in colors_dict.items()}
def color_name(color):
  a = 255 // len(list(colors_dict.keys()))
  for i in [hex2rgb(i) for i in inversed_color.keys()]:
      if color[0] in range(i[0] - a, i[0] + a) and color[1] in range(i[1] - a,i[1] + a) and color[2] in range(i[2] - a,i[2] + a):
         return inversed_color[rgb2hex(i[0],i[1],i[2])]
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
    st.write("color name is : " + str(color_name(rgb2hex(colors[a][0],colors[a][1],colors[a][2])))))
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.asarray(image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    colors(image,most_frequent=most)
    
    st.balloons()
