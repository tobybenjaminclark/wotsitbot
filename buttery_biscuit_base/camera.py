from picamera2 import Picamera2
import io

class CameraFeed:
    def __init__(self):
        self.camera = Picamera2()

        video_config = self.camera.create_video_configuration(main={"size": (1080, 480)})
        self.camera.configure(video_config)

        self.camera.start()

    def get_current_image_bytes(self):
        data = io.BytesIO()
        self.camera.capture_file(data, format='jpeg')
        data.seek(0)
        return data.read()

    def __del__(self):
        self.camera.stop()