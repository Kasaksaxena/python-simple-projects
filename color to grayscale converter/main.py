import streamlit as st 
from  PIL  import Image 

st.subheader("Color to grayscale converter")

# Create a file uploader component allowing the user
uploaded_image=st.file_uploader("Upload Image")
with st.expander("Start camera"):
 camera_image=st.camera_input("Camera")
 
if camera_image:
  img=Image.open(camera_image)
  gray_image=img.convert("L")
  st.image(gray_image)
  
if uploaded_image:
    # Open the user uploaded image with PIL
    img=Image.open(uploaded_image)  
  # Convert the image to grayscale
    gray_uploaded_img=img.convert("L")
    # Convert the image to grayscale
    st.image(gray_uploaded_img)



