import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def show_hist(img, hist):
    '''
    显示图片与图片对应的灰度图像
    :param img:
    :param hist:
    :return:
    '''
    plt.subplot(121)
    plt.imshow(img, 'gray')
    plt.subplot(122)
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()

def get_hist(img):
    return cv.calcHist([img], [0], None, [256], [0,256])



if __name__ == "__main__":
    IMG_PATH = r"C:\Users\amjt_zhao\Desktop\sick_chiken.jpg"
    img = cv.imread(IMG_PATH, 0)
    print(img.shape)

    if img is None:
        print("找不大图片啊！大人", IMG_PATH)
        exit(111)

    show_hist(img, get_hist(img))