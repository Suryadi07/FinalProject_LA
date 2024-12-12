import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
from PIL import Image

members = [
    {"name": "Adetia Yuni Pangesti", "role": "Developer"},
    {"name": "Ariq Saepul Aziz", "role": "Data Scientist"},
    {"name": "Puji Nur Hadiyah", "role": "Tester"},
    {"name": "Sugiyanto", "role": "Ngopi"}
]

# halaman tranformation
def apply_transformations(image, zoom, angle, tx, ty, skew_x, skew_y):
    h, w = image.shape[:2]

    # fungsi zoom
    zoom_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), 0, zoom)
    image = cv2.warpAffine(image, zoom_matrix, (w, h))

    # fungsi rotasi
    rot_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    image = cv2.warpAffine(image, rot_matrix, (w, h))

    # Fungsi translasi
    trans_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    image = cv2.warpAffine(image, trans_matrix, (w, h))

    # Fungsi Skewing
    skew_matrix = np.float32([
        [1, skew_x, 0],
        [skew_y, 1, 0]
    ])
    image = cv2.warpAffine(image, skew_matrix, (w, h))

    return image

# halaman menampilkan streamlit
st.set_page_config(page_title="Image Processing App", layout="wide")

# navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload & Transform"])

if page == "Upload & Transform":
    st.title("Image Processing App Group 6")

    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Read the image
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        st.sidebar.header("Transformations")

        # Zoom
        zoom = st.sidebar.slider("Zoom", 0.1, 3.0, 1.0, 0.1)

        # Rotation
        angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)

        # Translation
        tx = st.sidebar.slider("Translate X", -200, 200, 0)
        ty = st.sidebar.slider("Translate Y", -200, 200, 0)

        # Skewing
        skew_x = st.sidebar.slider("Skew X", -0.5, 0.5, 0.0, 0.01)
        skew_y = st.sidebar.slider("Skew Y", -0.5, 0.5, 0.0, 0.01)

        # Apply transformations
        transformed_image = apply_transformations(image_np, zoom, angle, tx, ty, skew_x, skew_y)

        # Menampilkan gambar asli dan diubah
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image, caption="Original Image", use_column_width=True)

        with col2:
            st.subheader("Transformed Image")
            st.image(transformed_image, caption="Transformed Image", use_column_width=True)

elif page == "Home":
   st.title("Selamat datang")
   st.write("Selamat datang di aplikasi pengolahan gambar Group 6! Pilih menu di sebelah kiri untuk memulai.")
   for member in members:
        st.subheader(member["name"])
        st.write(f"Role: {member['role']}")