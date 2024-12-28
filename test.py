from PIL import Image
import torchvision.transforms as transforms
import numpy as np
import torch
# 打开图片
image_path = r'E:\mydjango\Picture_Processor\image\a1.jpg'  # 替换为你的图像文件路径
image = Image.open(image_path).convert('RGB')
numpy_array = np.array(image)
print(numpy_array)

# tensor_image = torch.from_numpy(numpy_array)
# print(tensor_image.shape)
# 定义转换操作：将图片转换为张量
# transform = transforms.ToTensor()

# 应用转换操作
# tensor_image = transform(image)

# print(tensor_image.shape)