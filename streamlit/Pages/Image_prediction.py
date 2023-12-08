import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import io

# Load the saved model
save_model = load_model("E:\\Project\\MiniProject\\fire\\my_keras_model.h5")
st.markdown("<h1 style='text-align: center; color: black;'>Image Prediction</h1>", unsafe_allow_html=True)
def predict_single_image(image_path):
    image = Image.open(image_path)
    image = np.array(image.convert('RGB'))
    image = cv2.resize(image, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR
    image_array = np.expand_dims(image, axis=0)
    prediction = save_model.predict(image_array)
    predicted_class = 'non-fire' if prediction[0][0] >= 0.5 else 'fire'

    st.image(image, caption=f'Predicted Class: {predicted_class}', use_column_width=True)

def main():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png","jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        predict_single_image(uploaded_file)

if __name__ == '__main__':
    main()
