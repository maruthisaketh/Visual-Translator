from langdetect import detect, DetectorFactory


DetectorFactory.seed = 0

def translate_text(text):

    try:
        text_lines = text.split("\n")
        for line in text_lines:
            print(line)
            if line:
                print(detect(line))
    
    except Exception as e:
        print(e)