import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv


def my_defined_filter(img, scal=5):
    kernel = np.ones((scal, scal), np.float32) / pow(5,2)
    return cv.filter2D(img, -1, kernel)

def normal_filter(img, scal=3):
    return cv.GaussianBlur(img, (scal, scal), 0)

def median_filter(img, scal=3):
    return  cv.medianBlur(img, scal)