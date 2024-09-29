# OCR and Document Search Web Application

## Setup Instructions

1. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install necessary Python packages.

2. **Install Tesseract OCR:**
   - **Windows:** Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   - **macOS:** Run `brew install tesseract`.
   - **Linux:** Run `sudo apt-get install tesseract-ocr`.
   - Ensure Tesseract is added to your PATH.

3. **Run the Application Locally:**
   - Execute `streamlit run app.py` in your terminal.

4. **Deployment Instructions:**
   - Deploy the application using platforms like Streamlit Sharing or Hugging Face Spaces. Follow their specific instructions for deployment.

## Application Functionality

- The application allows users to upload images, extract text using OCR, and perform keyword searches within the extracted text.

## Additional Notes
- If the application does not detect Tesseract, ensure it is properly installed and added to the system's PATH.
