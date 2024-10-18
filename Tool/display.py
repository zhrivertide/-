import cv2 as cv
from matplotlib import pyplot as plt

def show_img_plt(img):
    """
    :param img:plt可以输出float类型数据
    :return:
    """
    plt.figure(figsize=(5,5))
    plt.imshow(img, cmap='gray')
    plt.show()
def show_two_plt(img1, img2):
    plt.figure(figsize=(9,5))
    plt.subplot(121)
    plt.imshow(img1, cmap='gray')
    plt.subplot(122)
    plt.imshow(img2, cmap='gray')
    plt.show()

def show_img_cv(img):
    """
    :param img: cv只可以输出格式为uint8的numpy类型数据
    :return:
    """
    cv.imshow("img", img)
    kb = cv.waitKey(0)
    if kb == 'q':
        cv.destroyWindow("img")
    elif kb == 'a':
        cv.destroyAllWindows()
    elif kb == 's':
        cv.imwrite('./img.png', img)
        cv.destroyAllWindows()