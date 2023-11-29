import streamlit as st
from PIL import Image
import pickle as pkl
import numpy

class_list = {'0': 'Normal','1': 'Pneumonia'}

st.title('Pneumonia Detecion')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

st.header('Upload an image')
image = st.file_uploader('Choose an image', type=(['png', 'jpg', 'jpeg']))

if image is not None:
  image = Image.open(image)
  st.image(image, caption='Test image')

  if st.button('Predict'):
    image = image.resize((227*227*3, 1))
    vector = 
