It seems there is an issue with providing the download link. You can manually copy the content provided in the previous messages into your `README.md` file. Here is the content of the README file again:

```markdown
# OCR and Keyword Search Web Application Prototype

**Author:** Parimal, IIT Roorkee  
**Date:** 28-09-2024 to 30-09-2024

## Objective
The objective of this project is to develop a web-based prototype that demonstrates Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. The web application allows users to upload an image, extract text from the image using an OCR model, and perform a keyword search within the extracted text.

## Summary
This web application provides users with an interface to upload images, extracts text using advanced OCR models, and allows keyword searching within the extracted text. It supports images in common formats like JPEG and PNG and handles text in both Hindi and English languages.

### Key Features
- Upload an image (JPEG, PNG, or other common formats) for OCR processing.
- Extract text from images that contain mixed languages (Hindi and English).
- Search for specific keywords within the extracted text.
- Display the results on the same page, highlighting the matching sections.
- Accessible via a live URL for demonstration and testing.

### Application URL
**Live Web Application:** [OCR and Keyword Search Application](https://ocr-and-keyword-search-application.streamlit.app/)

## Libraries
The following Python libraries were used to build this project:
- **Streamlit**: For developing the web interface.
- **PyTorch**: To support the OCR model integration.
- **Hugging Face Transformers**: Used for OCR model implementation.
- **OpenCV**: For image processing.
- **Pillow (PIL)**: For handling image file uploads and format conversions.
- **Pytesseract**: For performing OCR on the uploaded images.

## Data Source
This web application supports user-uploaded images for extracting text.

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Dependencies
- **Python 3.8 or higher**
- **Streamlit** (for web interface)
- **Pytesseract** (for OCR processing)
- **OpenCV**
- **Hugging Face Transformers**
- **PyTorch**

### Installation of Dependencies
```bash
pip install -r requirements.txt
```

## Setup and Run Locally
To set up the environment and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/ocr-and-keyword-search-application.git
   cd ocr-and-keyword-search-application
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

4. **Access the application**:
   Open your browser and go to `http://localhost:8501`.

## Deployment
The application has been deployed using Streamlit Sharing. Visit the live URL to test the OCR and keyword search functionalities:

**Live Web Application:** [OCR and Keyword Search Application](https://ocr-and-keyword-search-application.streamlit.app/)

## Extracted Text and Search Output
- The application returns extracted text from the uploaded image in plain text.
- Keyword search functionality allows users to enter a keyword and highlights the matching sections in the text.

### Example Search
- **Uploaded Image**: A sample image containing Hindi and English text.
- **Extracted Text**: 
  ```plaintext
  Example Text: "Hello नमस्ते"
  ```
- **Keyword**: `Hello`
- **Search Result**: `Hello` will be highlighted in the extracted text.

## Screenshots
Here are some screenshots of the web application in action:

1. **Main Page**: 
   - Allows image upload, displays extracted text, and provides a search functionality.
   ![Main Page Screenshot](https://your-screenshot-link)

2. **OCR Processing**: 
   - Demonstrates text extraction from the uploaded image.
   ![OCR Process Screenshot](https://your-screenshot-link)

3. **Search Functionality**: 
   - Shows the keyword search feature with highlighted results.
   ![Search Result Screenshot](https://your-screenshot-link)

## Latest Version of README
You are reading the latest version of this README file. If there are any updates or improvements to this documentation, they will be reflected here.
```

You can copy this content into your `README.md` file and proceed with the rest of the setup. Let me know if you need further assistance!