import cv2 as cv
import numpy as np
import openpyxl 
wb = openpyxl.Workbook()
ws = wb.active
l1img = cv.imread("Level1.png")
cv.imshow("Original", l1img)
width = l1img.shape[1]
height = l1img.shape[0]
grayScale = np.zeros([height,width], dtype=np.uint8)

for i in range(height):
    for j in range(width):
        sum = 0
        for k in range(3):
            sum += l1img[i][j][k]
        grayVal = int(sum/3)
        grayScale[i][j] = grayVal
        ws.cell(row=i+1,column=j+1).value = grayVal
print(grayScale[6][94])
print(l1img[6][94])
wb.save('pixelVals.xlsx')
cv.imshow("Grayscale", grayScale)
cv.waitKey(0)
