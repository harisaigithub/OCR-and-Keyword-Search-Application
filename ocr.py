import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import re
from PIL import Image as PILImage
from io import BytesIO

def pre_process_image(image):
    """
    Pre-process the image to improve OCR accuracy.
    Convert to grayscale, apply thresholding, and denoise.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Denoising
    denoised = cv2.fastNlMeansDenoising(thresh, h=30)
    
    return denoised

def enhanced_ocr(image_input):
    """
    Enhanced OCR function with pre-processing and post-processing.
    Handles both file paths and BytesIO streams.
    """
    if isinstance(image_input, str):  # Image from file path
        image = cv2.imread(image_input)
    else:  # Image from uploaded file (BytesIO stream)
        image = np.array(PILImage.open(BytesIO(image_input.read())))

    # Pre-process the image
    processed_image = pre_process_image(image)
    
    # Perform OCR
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_image, config=custom_config)

    # Post-processing: Fix common OCR errors
    text = post_process_text(text)
    
    return text

def post_process_text(text):
    """
    Post-process the OCR extracted text to correct common OCR errors.
    """
    # Example: Correct common OCR mistakes
    replacements = {
        "0": "O",
        "1": "I",
        "l": "I",
        "5": "S",
        "$": "S",
        "@": "a",
        "©": "c"
    }
    
    for original, corrected in replacements.items():
        text = re.sub(rf'\b{original}\b', corrected, text)
    
    # Additional post-processing (e.g., spell-checking) can be done here
    
    return text
