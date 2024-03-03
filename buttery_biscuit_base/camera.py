import cv2

class CameraFeed:
    feed = cv2.VideoCapture(0) 

    def get_current_image_bytes(self):
        ret, frame = self.feed.read()

        return cv2.imencode('.png', frame)[1]