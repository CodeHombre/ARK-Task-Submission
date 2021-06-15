import pydub
import cv2 as cv
import numpy as np

treasurePNG = cv.imread("treasure_mp3.png",0)


song = pydub.AudioSegment(treasurePNG.tobytes(),frame_rate=44100,sample_width=2,channels=1)
song.export("treasure.mp3",format="mp3",bitrate="320k")


