from src.image_text import extract_text

def runOCR():
    try:
        extract_text()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    runOCR()