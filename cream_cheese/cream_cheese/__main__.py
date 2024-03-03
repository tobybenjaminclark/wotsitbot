import cv2

feed = cv2.VideoCapture(0) 

def main():
    while True:
        ret, frame = feed.read()

        cv2.imencode('.jpg', frame)[1]