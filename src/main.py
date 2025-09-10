from image_text import extract_text
from video_text import extract_text_from_video

def runOCR():
    try:
        extract_text()
        extract_text_from_video()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    runOCR()