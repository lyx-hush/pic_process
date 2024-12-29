import torch
from torchvision import models, transforms
from PIL import Image
import timm
from timm import create_model


def get_labels(en=False):
    labels = []
    with open('class_comparison_tabel_zh_imagenet1k', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
            if en:
                label = line.split(' ')[-2]
                # print(label)
                labels.append(label.strip('\n'))

            else:
                label = line.split(' ')[-1]
                # print(label)
                labels.append(label.strip('\n'))
    file.close()
    return labels


def vit_inference(img,model):
    model_name = 'vit_base_patch16_224'  # 你可以根据需要选择不同的ViT模型
    model = create_model(model_name, pretrained=False, checkpoint_path='../checkpoint/vit_b_16_224_1k.safetensors')
    model_path = '../checkpoint/vit_b_16_224_1k.safetensors'

    # 加载模型权重
    # checkpoint = torch.load(model_path, map_location='cpu')  # 使用'cpu'以确保权重在CPU上加载
    #
    # # 应用模型权重
    # model.load_state_dict(checkpoint['state_dict'])
    model.eval()
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(img)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        outputs = model(input_batch)

    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    # 获取预测类别的索引
    _, predicted_class_idx = torch.max(probabilities, dim=0)

    # 获取类别名称（你需要有一个映射ImageNet类别ID到名称的字典）
    # 这里只是一个示例，你需要根据你的模型和数据集下载或定义相应的类名列表
    class_names = get_labels()  # 替换为实际的类别名称

    # 输出预测结果
    predicted_class = class_names[predicted_class_idx.item()]
    print(f'Predicted class: {predicted_class}')


if __name__ == '__main__':
    image_path = r'E:\mydjango\Picture_Processor\image\ceshi.jpg'
    image = Image.open(image_path).convert('RGB')
    vit_inference(image)
    # labels = get_labels()
    # print(labels)
