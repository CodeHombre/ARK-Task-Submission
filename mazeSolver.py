import cv2 as cv
import numpy as np

maze = cv.imread("Maze_BW.png",0)


#start point = (9,159)
#end point = (9+3*146,159)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

start = [9,159]
end = [9+3*146,159]

def pathBlock(p):
    for i in range(-1,2):
        for j in range(-1,2):
            maze[p[1]+i][p[0]+j] = 80

def color(p):
    return maze[p[1]][p[0]]

def search(start,end,maze):
    isFound = False
    path = []
    visited = []
    current = start

 
    while not isFound:
        if current not in visited:
            visited.append(current)
        if current not in path:
            path.append(current)
        possible = []
        neighbours = [[current[0]+3,current[1]],
                      [current[0]-3,current[1]],
                      [current[0],current[1]+3],
                      [current[0],current[1]-3]]
        
        for move in neighbours:
            if(move[0]==end[0] and move[1]==end[1]):
                isFound = True
                for p in path:
                    pathBlock(p)
                return maze
            elif(color(move)==255 and color(move) != 0):
                if(move not in visited):
                    possible.append(move)
        
        if len(possible)==1:
            current = possible[0]
        
        elif len(possible)==0:
            current = path[path.index(current)-1]
            path = path[:path.index(current)]
        else:
            i = np.random.randint(0,len(possible)-1)
            current = possible[i]

solvedMaze = search(start,end,maze)

cv.imshow("Maze",solvedMaze)
cv.imwrite("SolvedMaze_DFS.png",solvedMaze)                     
cv.waitKey(0)
