import cv2
import pytesseract
from matplotlib import pyplot as plt
import sys, os
from langdetect import detect, DetectorFactory
import subprocess

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

DetectorFactory.seed = 0

def get_installed_tesseract_languages():
    out = subprocess.check_output(['tesseract', "--list-langs"], text=True)
    langs = out.strip().split("\n")[1:]
    return langs

def extract_text_from_image():

    try:

        #Read the image
        image_path = "..\\..\\assets\\jpn.png"
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #Convert image to Grayscale
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

        # Apply thresholding for better contrast
        _, image_gray = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        #Display Original image
        #cv2.imshow('Original', image_rgb)

        #Display Gray Image
        #cv2.imshow('Gray Scale', image_gray)

        langs="+".join(get_installed_tesseract_languages())

        #Extract Text from Image
        extracted_text = pytesseract.image_to_string(image_gray, lang=langs)

        # #Draw Bounding Boxes around the text in image
        # data = pytesseract.image_to_data(image_gray, output_type=pytesseract.Output.DICT)

        # n_boxes = len(data['level'])
        # for i in range(n_boxes):
        #     (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        #     cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

        
        #Display the image with bounding boxes
        # plt.figure(figsize=(10, 6))
        # plt.imshow(image_rgb)
        # plt.title("Image with Text Bounding Boxes")
        # plt.axis("off")
        # plt.show()

        return extracted_text
    except pytesseract.TesseractNotFoundError:
        return "Tesseract OCR engine not found. Please ensure it's installed and in your PATH."
    
    except FileNotFoundError:
        return f"Image not found at: {image_path}"
    
    except Exception as e:
        # Get Exception type, Exception message, Exception text from exception info
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        # Print Exception type, File name where exception occurred and line number
        print("------------Exception Occurred-----------------")
        print("Exception Type:", exc_type)
        print("Filename:", fname)
        print("Exception Line:", exc_tb.tb_lineno)
        print("Exception Object:", exc_obj)