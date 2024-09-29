import streamlit as st
from ocr import enhanced_ocr
from PIL import Image, UnidentifiedImageError
import os
import base64
from io import BytesIO
from search import search_keywords  # <-- Importing search_keywords function

# Function to encode images into base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Encode the images
github_logo_encoded = encode_image("static/images/github-logo.png")
linkedin_logo_encoded = encode_image("static/images/linkedin-logo.png")
website_logo_encoded = encode_image("static/images/website-logo.png")

# Initialize session state for sample_image if not already set
if "sample_image" not in st.session_state:
    st.session_state["sample_image"] = "None"

# Inject Google Fonts, custom CSS, and custom cursors
st.markdown('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap">', unsafe_allow_html=True)
st.markdown('<style>{}</style>'.format(open('static/style.css').read()), unsafe_allow_html=True)

# Custom HTML header for consistent style with other HTML parts
st.markdown("""
    <div class="wrapper">
        <header>
            <div class="header-container">
                <h1>OCR and Keyword Search Application</h1>
                <p class="subtitle">Extract Text from Images</p>
            </div>
        </header>
""", unsafe_allow_html=True)

# Main content container
with st.container():
    st.markdown("<h2 class='title'>Extract Text from Images</h2>", unsafe_allow_html=True)

    # Ensure the 'samples' directory exists
    samples_dir = 'samples'
    if not os.path.exists(samples_dir):
        st.warning(f"The '{samples_dir}' directory does not exist. Please create it and add sample images.")
        sample_images = []
    else:
        sample_images = os.listdir(samples_dir)

    # File uploader for image upload
    uploaded_file = st.file_uploader("Or upload an image...", type=["jpg", "png", "jpeg"])

    # Automatically reset sample selection to "None" if a new image is uploaded
    if uploaded_file:
        st.session_state["sample_image"] = "None"

    # Display sample images for selection
    sample_selection = st.selectbox("Choose a sample image:", ["None"] + sample_images, key="sample_image")

    # Logic to determine which image to process
    image = None
    image_path = None

    # Handle sample image selection
    if st.session_state["sample_image"] != "None":
        image_path = os.path.join(samples_dir, st.session_state["sample_image"])
        try:
            image = Image.open(image_path)
            st.image(image, caption='Selected Sample Image', use_column_width=True)
        except UnidentifiedImageError:
            st.error(f"Error: Could not open or identify the image file '{st.session_state['sample_image']}'.")

    # Handle file upload
    elif uploaded_file is not None:
        try:
            # Read the uploaded file and display it
            bytes_data = uploaded_file.read()  # Read the uploaded file's bytes
            image = Image.open(BytesIO(bytes_data))  # Open the image
            st.image(image, caption='Uploaded Image', use_column_width=True)
        except UnidentifiedImageError:
            st.error("Error: Could not open or identify the uploaded image.")

    # Perform OCR if an image is available
    if image:
        if st.session_state["sample_image"] != "None":
            # Use path for sample image
            text = enhanced_ocr(image_path)
        else:
            # Use the uploaded image bytes directly for OCR
            text = enhanced_ocr(BytesIO(bytes_data))  # Pass the image bytes to OCR function

        # Display extracted text
        st.text_area("Extracted Text", text, height=200)

        # Keyword Search Feature
        keyword = st.text_input("Enter keyword to search")
        if keyword:
            # Use the updated search_keywords function to find sentences instead of lines
            matching_sentences = search_keywords(text, keyword)
            
            if matching_sentences:
                # Highlight the keyword in the sentences
                highlighted_sentences = [
                    sentence.replace(keyword, f"<mark>{keyword}</mark>") for sentence in matching_sentences
                ]
                st.markdown("<br>".join(highlighted_sentences), unsafe_allow_html=True)
            else:
                st.write("No sentences found containing the keyword.")

# Footer
st.markdown("""
    <footer style="background-color: #333; color: white; padding: 10px; width: 100%; position: fixed; bottom: 0; left: 0; display: flex; justify-content: space-between; align-items: center; padding: .2rem 35px; box-sizing: border-box; font-size: 16px;">
        <div style="text-align: left;">
            <p style="margin: 0;">&copy; 2024 OCR and Keyword Search Application</p>
        </div>
        <div style="text-align: center; flex-grow: 1;">
            <p style="margin: 0;">This website is made with ❤️ by P. Hari Sai 💪🤞</p>
        </div>
        <div class="social-links" style="display: flex; gap: 20px; justify-content: flex-end; align-items: center;">
            <a href="https://github.com/harisaigithub" target="_blank" style="text-align: center;">
                <img src="data:image/png;base64,{}" alt="GitHub" width="40" height="40" style="display: block; margin: 0 auto;">
                <span style="font-size: 14px;">GitHub</span>
            </a>
            <a href="https://www.linkedin.com/in/parasa-hari-sai" target="_blank" style="text-align: center;">
                <img src="data:image/png;base64,{}" alt="LinkedIn" width="40" height="40" style="display: block; margin: 0 auto;">
                <span style="font-size: 14px;">LinkedIn</span>
            </a>
            <a href="https://parasa-harisai-portfolio.netlify.app/" target="_blank" style="text-align: center;">
                <img src="data:image/png;base64,{}" alt="Portfolio" width="40" height="40" style="display: block; margin: 0 auto;">
                <span style="font-size: 14px;">Portfolio</span>
            </a>
        </div>
    </footer>
""".format(github_logo_encoded, linkedin_logo_encoded, website_logo_encoded), unsafe_allow_html=True)
