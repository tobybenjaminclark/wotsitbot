import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera

class CameraFeed:
    camera = PiCamera()

    def get_current_image_bytes(self):
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format="bgr")

        return cv2.imencode('.png', rawCapture.array)[1]