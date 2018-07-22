# -*- coding=GBK -*-
import cv2 as cv
import time
import threading as th
import sys

src = cv.imread("../input/IMG_0555.JPG")

print(src.shape)
print(src.size)
print(src.dtype)

#cv.line(src, (0,0), (100,100), (255,0,0), 2)
#cv.circle(src,(100,100),63,(0,0,255), 2)
#font = cv.FONT_HERSHEY_SIMPLEX
#cv.putText(src,"OpenCv", (100,100), font, 5, (0,0,255), 2)


def mouse_cb(event, x, y, flags, param):
    cv.circle(src,(x,y),2,(0,0,255), 2)
    cv.imshow("test1", src)

r, g, b = cv.split(src)

cv.namedWindow("test1") ## , cv.WINDOW_NORMAL
#cv.setMouseCallback("test1", mouse_cb)

##numpy 操作
color1 = src[:, :,1]
#src[:, :, 0] = 0
#src[:, :, 1] = 0
#src[:, :, 2] = 0

#copy_test = src[300:400, 300:400]
#src[0:100, 0:100] = copy_test

cv.rectangle(src,(300,300),(400,400),(0,255,0),-1)
for i in range(0,30):
    for j in range(0,30):
        src.itemset((350 + i,350 + j, 0), 0)
        src.itemset((350 + i,350 + j, 1), 0)
        src.itemset((350 + i,350 + j, 2), 255)



cv.imshow("test1", src)

src2 = cv.imread("../input/IMG_0570.JPG")

cut_src1 = src[0:300,0:300]
cut_src2 = src2[0:300,0:300]

i = 0

def display_img():
    global i
    tmp = i/100.0
    i = i+1

    dst = cv.addWeighted(cut_src1, tmp, cut_src2, 1-tmp, 0)
    cv.imshow("test1", dst)
    if i <= 100:
        return 0
    else:
        return 1


def time_cb():
    global timer
    if display_img() == 0:
        timer = th.Timer(0.1,time_cb)
        timer.start()
    else:
        print("will exit")

timer = th.Timer(1,time_cb)
timer.start()

cv.waitKey()

cv.destroyAllWindows()
sys.exit(0)


