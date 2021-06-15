from re import M
import numpy as np
import cv2 as cv

level2 = cv.imread("Level2_Img.png")
level2_gray = cv.cvtColor(level2,cv.COLOR_BGR2GRAY)
cv.imshow("L2",level2)
zucky_elon = cv.imread("zucky_elon.png")
# mRows = zucky_elon.shape[0]
# mCols = zucky_elon.shape[1]
# target = zucky_elon[2*mRows//5:4*mRows//5,0:mCols//3]
zucky_elon_gray = cv.cvtColor(zucky_elon,cv.COLOR_BGR2GRAY)
# cv.imshow("Zucky",target)


def match(img1,img2):
    XOR = cv.bitwise_xor(img1,img2)
    for i in range(XOR.shape[0]):
        for j in range(XOR.shape[1]):
            if(XOR[i][j]==1):
                return False
    return True

def find(img,target):
    height = target.shape[0]
    width = target.shape[1]
    for y in range(2*height//5,4*height//5-200):
        for x in range(width//3-150):
            cropped = target[y:y+200,x:x+150]
            if(match(cropped,img)):
                return(x,y)

print(find(level2_gray,zucky_elon_gray))
result = zucky_elon[460:660,230:380]
cv.imwrite("Result_found.png",result)

cv.waitKey(0)
