import os
from PIL import Image
import cv2
from pic_tool import PictureRead

image_path = '../image'


class ImageCVProcessor:
    def __init__(self, ):
        self.image = PictureRead()

    def cv_read(self):
        img = self.image.image_select(image_path=image_path)
