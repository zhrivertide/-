import cv2 as cv
import numpy as np
from Tool import show_img_plt, show_img_cv

if __name__ == "__main__":
    img_o = cv.imread("./rescourse/dou.png",1)
    if img_o is None:
        print("没图片哪")
    img = cv.cvtColor(img_o, cv.COLOR_BGR2GRAY)
    # 二值化OTSU法
    ret, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    print(f"阈值应该是{ret}")
    # 开运算：1、去除噪声 2、断开连接点
    kernel = np.ones((3, 3), np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
    # show_img_plt(opening)
    # 膨胀操作：确定背景区域
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    # 计算到边界的距离：寻找前景区域
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)
    # show_img_plt(sure_fg)
    # 背景-前景 -> 环形联通区域：找到未知区域
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)
    # 类别标记：标记联通区域的个数
    ret, markers = cv.connectedComponents(sure_fg)
    # 为所有的标记加1：前景目标从1开始标号【分水岭算法对物体的标注都大于1】
    markers = markers + 1
    # 现在让所有的未知区域为0
    markers[unknown == 255] = 0
    # 分水岭
    markers = cv.watershed(img_o, markers) # 分水岭后所有像素点被标记为-1
    img_o[markers == -1] = [255, 0, 0]
    show_img_cv(img_o)