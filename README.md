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
   ![Main Page Screenshot]![Screenshot (485)](https://github.com/user-attachments/assets/aaf823b3-56e9-476e-9f90-2a0e00869f7f)

2. **OCR Processing Using In-Built Samples Files**: 
   - Demonstrates text extraction from the sample image.
   - ![OCR Process Screenshot]![Screenshot (486)](https://github.com/user-attachments/assets/7040088b-a553-4b9b-8086-4d0441ba0f2b)
   
2.1 **Search Functionality**: 
   - Shows the keyword search feature with highlighted results.
   - ![OCR Process Screenshot]![Screenshot (487)](https://github.com/user-attachments/assets/e95a53df-ac74-4d64-a04c-d2d43fd68a52)
   - ![Screenshot (488)](https://github.com/user-attachments/assets/c19c1666-1057-40e6-92d2-a2ced644fb44)

3. **OCR Processing Using Upload Image**: 
   - Demonstrates text extraction from the uploaded image.
   - ![Screenshot (489)](https://github.com/user-attachments/assets/bee0a71a-9498-42be-b821-14bc0e7ff211)

3.1 **Search Functionality**: 
   - Shows the keyword search feature with highlighted results.
   - ![Screenshot (490)](https://github.com/user-attachments/assets/5c3c0f52-01aa-4117-87f0-2e5c59e770f2)
   - ![Screenshot (491)](https://github.com/user-attachments/assets/310fa513-465f-4bca-b46b-808151050ffa)
   - ![Screenshot (492)](https://github.com/user-attachments/assets/394df161-d897-4d78-80eb-00b46bcbddfd)

## VIDEO DEMOSTRATION:-
   -OUTPUT

https://github.com/user-attachments/assets/59e2b5d6-4573-4a3e-8a63-b93c0435e741





## Latest Version of README
You are reading the latest version of this README file. If there are any updates or improvements to this documentation, they will be reflected here.
```

You can copy this content into your `README.md` file and proceed with the rest of the setup. Let me know if you need further assistance!
