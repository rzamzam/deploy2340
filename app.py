
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load your trained machine learning model
model_path = 'fixedmodel.h5'
model = load_model(model_path)

# Function to preprocess the image and make predictions
def predict(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values between 0 and 1 (assuming your model expects this)

    predictions = model.predict(img_array)
    return predictions

# Streamlit app
def main():
    st.title('COVID-19 Pneumonia Detection App')

    # Upload an image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image_display = Image.open(uploaded_file)
        st.image(image_display, caption="Uploaded Image.", use_column_width=True)

        # Make predictions on the uploaded image
        predictions = predict(uploaded_file)

        st.subheader("Predictions:")
        # Assuming your model outputs probabilities for each class
        st.write(f"COVID-19 Probability: {predictions[0][0]:.2%}")
        st.write(f"Pneumonia Probability: {predictions[0][1]:.2%}")
        st.write(f"Normal Probability: {predictions[0][2]:.2%}")

if __name__ == "__main__":
    main()