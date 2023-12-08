# import streamlit as st
import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center; color: black;'>Model Report</h1>", unsafe_allow_html=True)

st.subheader('Model Accuracy and Loss in each Epoch')
image_path = "E:\\Project\\MiniProject\\fire\\accuracy.png" 
image = Image.open(image_path)
st.image(image)

st.subheader('Training and Validation Graph')
image_path_1 = "E:\\Project\\MiniProject\\fire\\graph.png"
image_1 = Image.open(image_path_1)
st.image(image_1)

st.subheader('Classification Report')
image_path_2 = "E:\\Project\\MiniProject\\fire\\classificait.png"
image_2 = Image.open(image_path_2)
st.image(image_2)

st.subheader('Confusion Matrix')
image_path_3 = "E:\\Project\\MiniProject\\fire\\confusion.png"
image_3 = Image.open(image_path_3)
st.image(image_3)
