import cv2

feed = cv2.VideoCapture(0) 

def main():
    while True:
        ret, frame = feed.read()
        