import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from display import show_img_plt, show_img_cv, show_two_plt
from Tool import get_hist, show_hist
def boundary_fill(img, baddingnum):
    return cv.copyMakeBorder(img, baddingnum, baddingnum, baddingnum, baddingnum, cv.BORDER_REPLICATE)

def add_gauss_noise(img):
    pass
def add_salt_noise(img,s_vs_p, amount):
    '''
    :param img: 只能添加灰度图，里面的矩阵是二维的，没有通道维度
    :param s_vs_p: #设置添加椒盐噪声的数目比例
    :param amount: #设置添加噪声图像像素的数目
    :return:
    '''
    noise_img = np.copy(img)
    rand = np.random.default_rng()
    #
    nums_salt = np.ceil(amount * img.size * s_vs_p)
    coords = [rand.integers(0, i-1, int(nums_salt)) for i in  img.shape]    # 设置添加噪声的坐标位置
    noise_img[coords[0], coords[1]] = 255
    #
    nums_pepper = np.ceil(amount * img.size * s_vs_p)
    coords = [rand.integers(0, i-1, int(nums_pepper)) for i in  img.shape]
    noise_img[coords[0], coords[1]] = 0
    return noise_img

if __name__ == "__main__":
    IMG_PATH = r"C:\Users\amjt_zhao\Desktop\sick_chiken.jpg"
    img = cv.imread(IMG_PATH, 0)
    # print(img.dtype)
    if img is None:
        print("找不大图片啊！大人", IMG_PATH)
        exit(111)
    print(img.shape)
    noise_img = add_salt_noise(img, 0.5,0.1)
    show_two_plt(noise_img, img)
