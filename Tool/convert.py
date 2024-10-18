import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def move_img(img, dx, dy):
    '''
    对图像进行平移操作
    | 1 0 dx|   *   |x|
    | 0 1 dy|       |y|
                    |1|
    :param img:
    :param dx: 左移动的距离
    :param dy: 下移动的距离
    :return:
    '''
    rows, cols = img.shape
    M = np.float32([[1,0,dx],[0,1,dy]])
    return cv.warpAffine(img, M, (cols, rows))

def spin(img, angle, flod = 1):
    rows, cols = img.shape
    M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), angle, flod)
    return cv.warpAffine(img, M, (cols, rows))
