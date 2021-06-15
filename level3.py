import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

l3 = cv.imread("maze_lv3.png")
cv.imshow("Noise Maze",l3)

def getColorHist(img):
    colors = ('b','g','r')
    for i,col in enumerate(colors):
        plt.figure()
        hist = cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist,color=col)
        plt.xlim([0,256])
    plt.show()

#getColorHist(l3)

def denoise_stage1(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = [img[i][j][0] - 217,0,0] 
    return img

denoised1 = denoise_stage1(l3)
cv.imshow("Denoised1",denoised1)

getColorHist(denoised1)
gray = cv.cvtColor(denoised1,cv.COLOR_BGR2GRAY)

# laplacian = cv.Laplacian(gray,cv.CV_64F)
# laplacian = np.uint8(np.absolute(laplacian))
# cv.imshow("Laplacian",laplacian)

#tried out averaging 
def denoise_stage2(img):
    kernel = np.ones((3,3),np.float32)/9
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            avg = 0
            count = 0
            for a in range(-2,3):
                for b in range(-2,3):
                    if((i+a)>=0 and (i+a)< img.shape[0]) and ((j+b)>=0 and (j+b) < img.shape[1]):
                        avg += img[i+a][j+b][0]
                        count += 1
            img[i][j][0] = int(avg/count)
    return img

# denoised2 = denoise_stage2(denoised1)
# cv.imshow("Denoised2",denoised2)

maze_bw = np.zeros(denoised1.shape[:2],np.uint8)
#got final maze here
for i in range(denoised1.shape[0]):
    for j in range(denoised1.shape[1]):
        if denoised1[i][j][0] >= 36:
            denoised1[i][j][0]= 230
            maze_bw[i][j] = 255
        else:
            denoised1[i][j][0] = 0
            maze_bw[i][j] = 0
    
print(denoised1)
cv.imshow("FINAL MAZE",denoised1)
cv.imwrite("Maze.png",denoised1)
cv.imwrite("Maze_BW.png",maze_bw)
getColorHist(denoised1)
cv.waitKey(0)
