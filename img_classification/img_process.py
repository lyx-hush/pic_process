from pic_tool import PictureRead
import os
from timm import create_model
import timm
import re

# model_checkpoint = './checkpoint'
module_path = os.path.abspath(__file__)
# 获取 img_process.py 文件所在的目录
module_dir = os.path.dirname(module_path)
# 构建 checkpoint 文件夹的绝对路径
model_checkpoint = os.path.join(module_dir, 'checkpoint')
print(model_checkpoint)
model_list = ['vit_base_patch16_224']
model_checkpoint_dict = {'vit_base_patch16_224': f'{model_checkpoint}/vit_b_16_224_1k.safetensors'}
print(model_checkpoint_dict)
def model_select():
    print('下列是模型列表:')
    temp = 0
    for index, model in enumerate(model_list):
        temp += 1
        print(f'{index + 1}:{model}')
    input_data = input('请输入想使用的模型名称或数字(退出输入):')
    if re.compile(r'^-?\d+$').match(input_data):
        print(1)
        if int(input_data) <= temp:
            model_name = model_list[int(input_data) - 1]
            model_checkpoint_path = model_checkpoint_dict[model_name]
            print()
            print(model_checkpoint_path)
            # model_name = 'vit_base_patch16_224'  # 你可以根据需要选择不同的ViT模型
            model = create_model(model_name, pretrained=False, checkpoint_path=model_checkpoint_path)
            print(f'创建模型{model_name}成功!')
            return 0, model
        else:
            print('超出范围,请重新输入！')
            return 1,None
    elif input_data in model_list:
        model_checkpoint_path = model_checkpoint_dict[input_data]
        # model_name = 'vit_base_patch16_224'  # 你可以根据需要选择不同的ViT模型
        model = create_model(input_data, pretrained=False, checkpoint_path=model_checkpoint_path)
        print(f'创建模型{input_data}成功!')
        return 1, model
    elif input_data == 'quit' or input_data == '退出':
        return -1, None
    else:
        print('请输入正确的序号或模型名称！')
        return 1, None


if __name__ == '__main__':
    # pass
    label = 1
    model = None
    while label == 1:
        label, model = model_select()
    # print(model)