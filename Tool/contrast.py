from pickletools import uint8

import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from display import show_img_plt, show_img_cv
from Tool import get_hist, show_hist
def change_contrast_brightness(img, alpha, beta):
    """线性变换，g(i,j) = alpha * f(i,j) + beta
        alpha:控制对比度
        beta:控制亮度    """
    try:
        if alpha < 1.0 or alpha > 3.0:
            raise ValueError("alpha must be between 1.0 and 3.0")
        if beta < 0 or beta > 100:
            raise ValueError("beta must be between 0 and 100")
    except ValueError as e:
        print(f"{str(e)}")
        exit(111)

    new_img = np.array(np.multiply(img, alpha) + beta, dtype=np.float32)

    # if img.ndim == 2:
    #     for y in range(img.shape[0]):
    #         for x in range(img.shape[1]):
    #             new_img[y,x] = alpha * img[y, x] + beta
    # elif img.ndim == 3:
    #     for y in range(img.shape[0]):
    #         for x in range(img.shape[1]):
    #             for c in range(img.shape[2]):
    #                 new_img[y,x,c] = alpha * img[y, x, c] + beta
    return new_img

def change_gamma(img, gamma=1):
    """
    伽马变换：用于将灰度过高或过低的图片进行修正，增强对比度 output = c * input ^ gamma
    gamma>1拉伸高灰度； gamma<1拉伸低灰度
    :param img: 原图
    :param gamma: 伽马系数
    :return: 修正图片
    """
    return np.array(np.power(img/255, gamma) * 255, dtype=np.uint8)

def bin_img(img):
    thresh, ret = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    return ret

if __name__ == "__main__":
    IMG_PATH = r"C:\Users\amjt_zhao\Desktop\sick_chiken.jpg"
    img = cv.imread(IMG_PATH, 0)
    print(img.dtype)
    if img is None:
        print("找不大图片啊！大人", IMG_PATH)
        exit(111)

    new_img = change_contrast_brightness(img, 2.5, 40)
    print(new_img.dtype)
    show_img_plt(new_img)
    # new_img = np.uint8(new_img)
    print(new_img.dtype)
    show_img_cv(new_img)

