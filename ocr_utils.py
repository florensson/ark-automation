from screen_verify import ImageVerifier as IV
import pytesseract
from PIL import ImageGrab, Image
import cv2
import numpy as np
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import re

region = (1764, 835, 55, 250)

def extract_int_from_ocr(text):
    match = re.search(r"\b(\d{2,4})\b", text)
    if match:
        return int(match.group(1))
    return None

def clean_ocr_text(text):
    text = text.replace('N', '11')
    # Vanliga OCR-fel som vi rättar upp
    replacements = {
        'O': '0', 'Q': '0', 'D': '0',
        'I': '1', '|': '1', 'l': '1',
        'S': '5', 'B': '8', 'f': '7',
        'F': '7'  # valfria extra om du märker dessa
    }
    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)
    return text

def read_text_from_region(region, lang='eng'):
    start = time.time()
    """
    Läser text med OCR från en viss region på skärmen.
    region = (x, y, width, height)
    """
    x, y, w, h = region
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))

    # Förbättra bilden för OCR
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    _, img_thresh = cv2.threshold(img_cv, 150, 255, cv2.THRESH_BINARY)

    # Konvertera tillbaka till PIL för pytesseract
    processed_img = Image.fromarray(img_thresh)

    raw_text = pytesseract.image_to_string(processed_img, config='--psm 6', lang=lang)
    cleaned_text = clean_ocr_text(raw_text)
    value = extract_int_from_ocr(cleaned_text)
    end = time.time()
    print(f"OCR read took {end - start} value: {value} and in text {cleaned_text}")
    return value


#time.sleep(3)
#for _ in range(1,100):
#    read_text_from_region(region)