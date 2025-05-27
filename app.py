import streamlit as st
from PIL import Image
import generate  # your existing generate.py file

st.set_page_config(page_title="Image Caption Generator", layout="centered")

st.title("🖼️ Image Caption Generator")
st.markdown("Upload an image and let the model generate a caption using deep learning.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    # Save uploaded file first
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Then open and show
    img = Image.open("temp.jpg")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Button to generate caption
    if st.button("Generate Caption"):
        st.write("Running model...")
        caption = generate.runModel("temp.jpg")
        st.success("Caption:")
        st.write(f"📜 *{caption}*")
