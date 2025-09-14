from image_text import extract_text_from_image, get_installed_tesseract_languages
from video_text import extract_text_from_video

def runOCR():
    try:

        #Get installed languages from tesseract
        langs = get_installed_tesseract_languages()

        #Extract text from images
        extracted_text = extract_text_from_image()
        
        #extract_text_from_video()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    runOCR()