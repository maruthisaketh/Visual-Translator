import cv2
import pytesseract
from matplotlib import pyplot as plt
import sys, os
import numpy as np

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

video_path = "..\\..\\assets\\video.mp4"

def extract_text_from_video():
    try:
        cap = cv2.VideoCapture(video_path)

        #Identify total number of frames
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Number of frames: {frame_count}")

        #Skip every 20 frames for smoother extractions
        frame_number = 0
        skip = 20

        #Run OCR only when there's significant frame difference as well
        prev_frame = None
        threshold = 10000

        while True:
            ret, frame = cap.read()
            if not ret:
                break  # video ended

            #Skip 20 frames
            frame_number += 1
            if frame_number % skip != 0:
                continue

            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            print("Why")

            if prev_frame is not None:
                print("Entered")
                # Optional: improve contrast & reduce noise
                gray = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                diff = cv2.absdiff(gray, prev_frame)
                non_zero_count = np.count_nonzero(diff)

                if non_zero_count > threshold:
                    # OCR
                    text = pytesseract.image_to_string(thresh, lang="eng")  # change to "jpn" for Japanese, etc.
                    if text.strip():
                        print("Detected Text:", text)


            prev_frame = gray
            
            # Show the video with bounding boxes (optional)
            cv2.imshow("Video", frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        cap.release()
        cv2.destroyAllWindows()


    except pytesseract.TesseractNotFoundError:
        return "Tesseract OCR engine not found. Please ensure it's installed and in your PATH."
    
    except FileNotFoundError:
        return f"Video not found at: {video_path}"
    
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
