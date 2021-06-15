import cv2 as cv
import numpy as np

maze = cv.imread("Maze_BW.png")
maze = cv.cvtColor(maze,cv.COLOR_BGR2GRAY)
h = maze.shape[0]
w = maze.shape[1]
cv.imshow("Maze",maze)

for i in range(11*h//12,h):
    for j in range(w):
        maze[i][j] = 255
cv.imshow("Modified",maze)

# start = maze[140:160,10:50]
# cv.imshow("crop",start)

# finish = maze[140:160,405:448]
# cv.imshow("finish",finish)

def clear(y1,y2,x1,x2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            maze[i][j] = 255

clear(140,161,10,51)
clear(140,161,405,449)


def block(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            maze[y+i][x+j] = 0
    
block(9+3*14,159-3*3) #completed a half filled obstacle

#start = (9,159)
#end = (9+3*146,159)
# length = 149
cv.imshow("Maze_Final",maze)
cv.imwrite("Maze_Final.png",maze)
cv.waitKey(0)
