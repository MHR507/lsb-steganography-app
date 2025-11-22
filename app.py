import streamlit as st
from PIL import Image
from stego.encoder import embed_data
from stego.decoder import extract_data
from stego.features import extract_features
from stego.detector import StegoDetector
import numpy as np
import io

st.title("LSB Image Steganography & Detection")

# Tabs for Encode / Decode / Detect
tab1, tab2, tab3 = st.tabs(["Encode", "Decode", "Detect"])

# ------------------- Encode -------------------
with tab1:
    st.header("Encode Payload into Image")
    cover_img_file = st.file_uploader("Upload Cover Image (PNG)", type=["png","jpg"])
    payload_text = st.text_area("Enter Payload Text")
    bits = st.slider("Bits per channel", 1, 2, 1)
    
    if st.button("Encode"):
        if cover_img_file and payload_text:
            # Save cover image temporarily
            cover_img = Image.open(cover_img_file)
            cover_img.save("temp_cover.png")
            
            # Embed payload
            output_path = "stego_temp.png"
            embed_data("temp_cover.png", payload_text, output_path, bits=bits)
            
            st.success("Payload encoded successfully!")
            st.image(output_path, caption="Stego Image")
            
            # ---------------- Download buttons ----------------
            # Download original cover image
            with open("temp_cover.png", "rb") as f:
                st.download_button(
                    label="Download Original Cover Image",
                    data=f,
                    file_name="cover_image.png",
                    mime="image/png"
                )
            
            # Download stego image
            with open(output_path, "rb") as f:
                st.download_button(
                    label="Download Stego Image",
                    data=f,
                    file_name="stego_image.png",
                    mime="image/png"
                )

# ------------------- Decode -------------------
with tab2:
    st.header("Decode Payload from Image")
    stego_img_file = st.file_uploader("Upload Stego Image (PNG)", type=["png","jpg"], key="decode")
    data_length = st.number_input("Enter Payload Length (characters)", min_value=1, value=5)
    bits_decode = st.slider("Bits per channel", 1, 2, 1, key="bits_decode")
    
    if st.button("Decode Payload"):
        if stego_img_file:
            stego_img = Image.open(stego_img_file)
            stego_img.save("temp_stego.png")
            payload = extract_data("temp_stego.png", int(data_length), bits=bits_decode)
            st.success("Payload extracted:")
            st.write(payload)

# ------------------- Detect -------------------
with tab3:
    st.header("Detect if Image is Stego or Cover")
    test_img_file = st.file_uploader("Upload Image", type=["png","jpg"], key="detect")
    
    if st.button("Run Detection"):
        if test_img_file:
            test_img = Image.open(test_img_file)
            test_img.save("temp_detect.png")
            features = extract_features("temp_detect.png").reshape(1,-1)
            
            detector = StegoDetector()
            detector.load("detector_model1.pkl")  # Pre-trained model
            pred = detector.predict(features)
            
            if pred[0] == 0:
                st.success("This is a COVER image.")
            else:
                st.error("This is a STEGO image.")
