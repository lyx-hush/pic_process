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
    def __init__(self):
        pass

    def read(self, thread=False, image_path=None):
        images = []
        if thread:
            pass
        elif os.path.isfile(image_path):
            print(f"对图像{image_path.split('/')[-1]}进行处理！")
            start_time = time.time()
            image = Image.open(image_path)
            end_time = time.time()
            print(end_time - start_time)
            return image
        elif os.path.isdir(image_path):
            start_time = time.time()
            directory = os.listdir(image_path)
            for filename in tqdm(directory):
                if filename.endswith(".jpg") or filename.endswith("png"):
                    image = Image.open(os.path.join(image_path, filename))
                    images.append(image)
                else:
                    continue
            end_time = time.time()
            print(end_time - start_time)
            return images

# if __name__ == '__main__':
#     pic_read = PictureRead(r'E:\mydjango\Picture_Processor\image')
#     images = pic_read.read()
#     tensor_list = pic_to_tensor(images)
#     print(tensor_list)
