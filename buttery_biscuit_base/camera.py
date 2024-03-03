from picamera2 import Picamera2
import cv2

class CameraFeed:
    def __init__(self):
        self.camera = Picamera2()

        self.camera.configure(self.camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.camera.start()

    def get_current_image_bytes(self):
        return cv2.imencode('.png', self.camera.capture_array())[1]