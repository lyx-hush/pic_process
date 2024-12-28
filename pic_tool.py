import os
from PIL import Image
from tqdm import tqdm
import time
import torch
import torchvision.transforms as transforms
import numpy as np


def pic_to_tensor(img):
    if isinstance(img, list):
        tensor_list = []
        for data in img:
            transform = transforms.ToTensor()
            print(type(data))
            transform_image = transform(data)
            tensor_list.append(transform_image)
        return tensor_list
    else:
        transform = transforms.ToTensor()
        transform_image = transform(img)
        return transform_image


def pic_to_np(img):
    if isinstance(img, list):
        np_list = []
        for data in img:
            np_img = np.array(data)
            np_list.append(np_img)
        return np_list
    else:
        np_img = np.array(img)
        return np_img


class PictureRead:
    def __init__(self, image_path):
        self.image_path = image_path

    def read(self, thread=False):
        images = []
        if thread:
            pass
        else:
            start_time = time.time()
            directory = os.listdir(self.image_path)
            for filename in tqdm(directory):
                image = Image.open(os.path.join(self.image_path, filename))
                images.append(image)
            end_time = time.time()
            print(end_time - start_time)
            return images


if __name__ == '__main__':
    pic_read = PictureRead(r'E:\mydjango\Picture_Processor\image')
    images = pic_read.read()
    tensor_list = pic_to_tensor(images)
    print(tensor_list)
