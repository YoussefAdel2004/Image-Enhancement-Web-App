# Image-Enhancement-Web-App
The Image Transformation Web App is an interactive web application built using Streamlit and OpenCV that allows users to upload an image and apply various image processing transformations and effects in real time.
Project Objectives

Provide an easy-to-use interface for image processing

Demonstrate fundamental OpenCV image transformations

Allow users to visually explore the effects of different filters

Enable real-time experimentation with parameters

# Technologies Used

Python 3

Streamlit – Web application framework

OpenCV (cv2) – Image processing

NumPy – Numerical operations

Pillow (PIL) – Image loading and handling

# Application Features
🔹 Image Upload

Supports image formats: JPG, JPEG, PNG

Uploaded images are displayed immediately

Automatic RGB conversion using Pillow

# Available Transformations & Effects
1️⃣ Color Space Conversions

BGR → Grayscale

BGR → RGB

BGR → HSV

BGR → LAB

2️⃣ Linear Transformations

Brightness adjustment using beta

Contrast adjustment using alpha

Formula used:

output = alpha × input + beta

3️⃣ Filters

Gaussian Blur

Adjustable kernel size

Bilateral Filter

Preserves edges while smoothing

Sharpening Filter

Enhances image details using convolution kernel

4️⃣ Image Effects

Negative Transformation

Inverts pixel values

Edge Detection (Canny)

Adjustable thresholds

Sepia Effect

Vintage-style color transformation

5️⃣ Additional Effects

Pencil Sketch Effect

Converts image into a hand-drawn sketch appearance

Uses grayscale conversion, inversion, blurring, and division

# Application Structure
image_transformer_app.py
│
├── apply_cvt_color()          # Color space conversion
├── apply_linear_transform()   # Brightness & contrast control
├── apply_negative_transform() # Negative image effect
├── main()                     # Streamlit UI & logic

▶️ How to Run the Application
1️⃣ Install Dependencies
pip install streamlit opencv-python numpy pillow

2️⃣ Run the App
streamlit run image_transformer_app.py

3️⃣ Open Browser

Streamlit will automatically open the app in your default browser.

# Error Handling

Handles unsupported color spaces gracefully

Displays user-friendly error messages using Streamlit alerts

Prevents crashes due to invalid input or processing failures



Integrate CNN-based image enhancement

Add batch image processing
