# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image
import numpy as np
import torch
import math
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
import cv2 as cv

# print(torch.randn(2,2,8))
# print(torch.__version__)
#
# writer = SummaryWriter("logs")
#
# for i in range(100):
#     writer.add_scalar("y=sin(x)",math.sin(i),i)
# writer.close()

img = Image.open("desk.png")
# cv.imshow("img1",img)
# print(img.shape)
# cv.waitKey()

img_resize_tran = transforms.Resize(128)
img_resize = img_resize_tran(img)
print(img_resize.size)
img_resize = np.array(img_resize)
cv.imshow("result", img_resize)
cv.waitKey()

