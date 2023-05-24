import random
from PIL import Image, ImageDraw
import os


def draw_lines(folder_path, save_path):
    # 遍历文件夹中的所有图像
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # 打开图像文件
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path).convert('RGB')

            # 获取图像大小
            width, height = img.size

            # 创建用于绘制的对象
            draw = ImageDraw.Draw(img)

            # 随机生成直线的起始点和结束点
            x1 = random.randint(0, width - 1)
            y1 = random.randint(0, height - 1)
            x2 = random.randint(0, width - 1)
            y2 = random.randint(0, height - 1)

            # 随机生成直线的颜色和宽度
            # r = random.randint(0, 255)
            # g = random.randint(0, 255)
            # b = random.randint(0, 255)
            # color = (r, g, b)

            width = random.randint(3, 8)

            # 画直线
            draw.line((x1, y1, x2, y2), fill='black', width=width)

            # 保存修改后的图像
            save_name = os.path.splitext(filename)[0] + '_line.jpg'
            save_pathname = os.path.join(save_path, save_name)
            img.save(save_pathname)

folder_path = r'E:\original'
save_path = r'E:\original_line'
draw_lines(folder_path, save_path)