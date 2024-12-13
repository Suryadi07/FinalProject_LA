import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
from PIL import Image

members = [
    {"name": "Adetia Yuni Pangesti", "foto": "1ade.jpeg"},
    {"name": "Ariq Saepul Aziz", "foto": "2ariq.jpeg"},
    {"name": "Puji Nur Hadiyah", "foto": "3puji.jpeg"},
    {"name": "Sugianto", "foto": "4sugi.jpeg"}
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

# tampilan bilah web
st.set_page_config(page_title="Image Processing App Group 6", layout="wide", page_icon="favicon.ico")

# navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Group Members", "Upload & Transform"])

if page == "Upload & Transform":
    st.title("Image Processing App Group 6")

    # Upload file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Read the image
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        st.sidebar.header("Transformations")

        # Zoom
        zoom = st.sidebar.slider("Zoom", 0.1, 3.0)

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
            st.image(image, caption="Original Image", use_container_width=True)

        with col2:
            st.subheader("Transformed Image")
            st.image(transformed_image, caption="Transformed Image", use_container_width=True)

#tulisan-tulisan yang ada di home
elif page == "Home":
    col1, col2 = st.columns([3, 7])
    with col1:
        st.image("pres.jpg", width=220)
    with col2:
        st.title("Welcome to the Website")
        st.title("Image Processing")
        st.markdown(
                f"""
                <p style='text-align: left; font-size: 18px; color: white; font-family: Roboto, cursive, sans-serif;'
                >{"This Streamlit application displays the results of the Image Processing project Majoring in Industrial Engineering Group 6. Explore the page to learn more about us, see the navigation panel !"}
                </p>
                """,
                unsafe_allow_html=True
            )
#menampilkan member di halaman ke 2
elif page == "Group Members":
    st.title("Group 6")
    st.subheader("Industrrial Engineering")
    st.subheader("Members:")
    member_cols = st.columns(len(members))
    for i, member in enumerate(members):
        with member_cols[i]:
            st.image(member["foto"], width=180)
            st.markdown(
                f"""
                <p style='text-align: left; font-size: 25px; color: white; font-family: Roboto, cursive, sans-serif;'>{member['name']}</p>
                """,
                unsafe_allow_html=True
            )       
