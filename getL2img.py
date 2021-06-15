import numpy as np
import cv2 as cv
import openpyxl

level1 = cv.imread("Level1.png")
imgMat = np.zeros((200,150,3),dtype=np.uint8)

i=0
j=0

flag = False
for r in range(6,level1.shape[0]):
    for c in range(level1.shape[1]):
        if(r==6 and c==94):
            flag = True
        if(flag):
            if(i<200 and j<150):
                imgMat[i][j] = level1[r][c]
                j += 1
                if(j==150):
                    j=0
                    i += 1

cv.imwrite("Level2_Img.png", imgMat)
cv.waitKey(0)
