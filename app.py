import streamlit as st
import cv2
import numpy as np
from PIL import Image

def apply_cvt_color(image, color_space):
    """Applies color space conversion using OpenCV."""
    try:
        if color_space == "BGR2GRAY":
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif color_space == "BGR2RGB":
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif color_space == "BGR2HSV":
            return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        elif color_space == "BGR2LAB":
            return cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        else:
            st.warning(f"Color space '{color_space}' not supported.")
            return image
    except Exception as e:
        st.error(f"Error applying color conversion: {e}")
        return image

def apply_linear_transform(image, alpha=1.0, beta=0):
    """Applies a linear transformation: output = alpha * input + beta."""
    try:
        transformed_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        return transformed_image
    except Exception as e:
        st.error(f"Error applying linear transformation: {e}")
        return image

def apply_negative_transform(image):
    """Applies negative transformation: output = 255 - input."""
    try:
        return 255 - image
    except Exception as e:
        st.error(f"Error applying negative transformation: {e}")
        return image

def main():
    st.set_page_config(page_title="Image Transformer", layout="wide")
    st.title("Image Transformation Web App")
    st.sidebar.header("Upload Image")

    uploaded_file = st.sidebar.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = np.array(Image.open(uploaded_file).convert('RGB'))
            st.image(image, caption="Original Image", use_column_width=True)

            st.sidebar.header("Transformations")
            tabs = st.tabs(["Color Space", "Linear Transform", "Filters", "Effects", "Additional Effects"])

            # Filters
            with tabs[2]:
                st.subheader("Filters")
                if st.checkbox("Apply Gaussian Blur"):
                    ksize = st.slider("Kernel Size (odd number):", 1, 31, 5, step=2)
                    transformed_image = cv2.GaussianBlur(image.copy(), (ksize, ksize), 0)
                    st.image(transformed_image, caption="After Gaussian Blur", use_column_width=True)

                if st.checkbox("Apply Bilateral Filter"):
                    d = st.slider("Diameter of pixel neighborhood:", 1, 15, 9)
                    sigma_color = st.slider("Sigma Color:", 1, 200, 75)
                    sigma_space = st.slider("Sigma Space:", 1, 200, 75)
                    transformed_image = cv2.bilateralFilter(image.copy(), d, sigma_color, sigma_space)
                    st.image(transformed_image, caption="After Bilateral Filter", use_column_width=True)

                if st.checkbox("Apply Sharpening"):
                    kernel = np.array([[0, -1, 0],
                                       [-1, 5, -1],
                                       [0, -1, 0]])
                    transformed_image = cv2.filter2D(image.copy(), -1, kernel)
                    st.image(transformed_image, caption="After Sharpening", use_column_width=True)

            # Effects
            with tabs[3]:
                st.subheader("Effects")
                if st.checkbox("Apply Negative Transformation"):
                    transformed_image = apply_negative_transform(image.copy())
                    st.image(transformed_image, caption="After Negative Transformation", use_column_width=True)

                if st.checkbox("Apply Edge Detection (Canny)"):
                    threshold1 = st.slider("Threshold1:", 0, 255, 50)
                    threshold2 = st.slider("Threshold2:", 0, 255, 150)
                    transformed_image = cv2.Canny(image.copy(), threshold1, threshold2)
                    st.image(transformed_image, caption="After Edge Detection", use_column_width=True, channels="GRAY")

                if st.checkbox("Apply Sepia Effect"):
                    sepia_filter = np.array([[0.272, 0.534, 0.131],
                                             [0.349, 0.686, 0.168],
                                             [0.393, 0.769, 0.189]])
                    transformed_image = cv2.transform(image.copy(), sepia_filter)
                    transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)
                    st.image(transformed_image, caption="After Sepia Effect", use_column_width=True)
#Trying to make another change
            with tabs[4]:             
                st.subheader("Additional Effects")
                if st.checkbox("Apply Pencil Sketch Effect"):
                    gray_image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
                    inverted_image = 255 - gray_image
                    blurred = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
                    inverted_blurred = 255 - blurred
                    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
                    st.image(sketch_image, caption="After Pencil Sketch Effect", use_column_width=True, channels="GRAY")       

        except Exception as e:
            st.error(f"Error loading or processing the image: {e}")
    else:
        st.info("Please upload an image to start.")

if __name__ == "__main__":
    main()