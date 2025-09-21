from image_text import extract_text_from_image, get_installed_tesseract_languages
from video_text import extract_text_from_video
from translate_text import translate_text

def runOCR():
    try:

        #Get installed languages from tesseract
        #langs = get_installed_tesseract_languages()

        #Extract text from images
        extracted_text = extract_text_from_image()
        print(extracted_text)

        #Detect Language for each line of extracted text
        translate_text(extracted_text)
        
        #Extract text from videos
        #extract_text_from_video()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    runOCR()