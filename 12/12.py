# -*- coding=GBK -*-
import cv2 as cv
import time
import threading as th
import sys
import numpy as np


e1 = cv.getTickCount()
time.sleep(1)
e2 = cv.getTickCount()

print((e2 - e1)/cv.getTickFrequency())

src = cv.imread("../input/IMG_0570.JPG")
hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV)

lower = np.array([0,200,200])
upper = np.array([30,255,255])
mask = cv.inRange(hsv, lower, upper)
res = cv.bitwise_and(src,src,mask = mask)

cv.namedWindow("test1")
cv.imshow("test1", res)

#使用鼠标取色彩的值
def mouse_cb(event, x, y, flags, param):
    print("x=" , x)
    print("y=" , y)
    cur_bgr = src[x, y]
    cur_bgr = np.array([[cur_bgr]])
    print("cur_bgr====", cur_bgr)
    #green = np.uint8([[[0,255,0]]])
    cur_hsv = cv.cvtColor(cur_bgr,cv.COLOR_BGR2HSV)
    print("cur_hsv====", cur_hsv)

#cv.setMouseCallback("test1", mouse_cb)

cv.waitKey()



cv.destroyAllWindows()
