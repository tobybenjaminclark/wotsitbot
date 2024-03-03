from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
import io

class CameraFeed:
    def __init__(self):
        self.camera = Picamera2()

        video_config = self.camera.create_video_configuration(main={"size": (1920, 1080)})
        self.camera.configure(video_config)

        encoder = JpegEncoder(q=70)

        self.bytes_io = io.BytesIO()

        self.camera.start_recording(encoder, self.bytes_io)

    def get_current_image_bytes(self):
        return self.bytes_io.read()

    def __del__(self):
        self.camera.stop_recording()