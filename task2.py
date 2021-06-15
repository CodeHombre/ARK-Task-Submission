import cv2 as cv
import numpy as np
import math
import sys

def draw_ball(img,x,y):
    cv.circle(img,(x,y),radius=50,color=(255,0,0),thickness=-1)

def detectFace(img):
    haar_cascade = cv.CascadeClassifier('haar_cascade_face.xml')
    face = haar_cascade.detectMultiScale(img,scaleFactor=1.1)
    for (x,y,w,h) in face:
        circle = [x+w//2,y+h//2,w//2]
        return circle

def getBallPosition(pos,vel,x_max,y_max,face_param):
    v = 20
    R = 50

    #collision with walls
    if(pos[0]>x_max-R or pos[0]<R):
        vel[0] = -vel[0]

    if(pos[1]>y_max-R or pos[1]<R):
        vel[1] = -vel[1]

    #collision with face
    a = face_param[0]
    b = face_param[1]
    r = face_param[2]
    d = math.sqrt((a-pos[0])**2 + (b-pos[1])**2)
    if(d<= (r+R)):
        vel[0] = (pos[0]-a)/d
        vel[1] = (pos[1]-b)/d
    
    pos[0] += int(vel[0]*v)
    pos[1] += int(vel[1]*v)
    
    return pos

def play():
    currPos = [100,100]
    vel = [1,1]
    isPlaying = True
    capture = cv.VideoCapture(0)

    while(True):
        isTrue, frame = capture.read()
        frame = cv.flip(frame,1)
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
        #tracking the ball
        face_coords = detectFace(gray)
        cv.circle(frame,(face_coords[0],face_coords[1]),radius=face_coords[2],color=(0,0,255),thickness=3)
        currPos = getBallPosition(currPos,vel,frame.shape[1],frame.shape[0],face_coords)
        if(isPlaying):
            draw_ball(frame,currPos[0],currPos[1])
        else:
            cv.putText(frame, 'GAME OVER',(frame.shape[0]//2-100,frame.shape[1]//2-200),cv.FONT_HERSHEY_SIMPLEX, 2.0,(50,50,50),4)


        #displaying frames
        cv.imshow("GAME",frame)

        #gameover
        if(currPos[1]>frame.shape[0]*4//5):
            isPlaying = False
        
        key = cv.waitKey(1)
        if key == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    play()
