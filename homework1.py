import cv2 as cv
import numpy as np
from Tool import get_hist

# 全局变量设置
IMG_PATH = r"C:\Users\amjt_zhao\Desktop\sick_chiken.jpg"

from Tool import *

if __name__ == "__main__":
    img = cv.imread(IMG_PATH, 1)
    if img is None:
        print("找不大图片啊！大人")
        exit(111)
    img_grad = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    # cv.imshow("sick chicken picture1", img)
    # kb = cv.waitKey(0)
    # cv.destroyWindow