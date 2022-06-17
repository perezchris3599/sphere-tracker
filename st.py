from collections import deque
from imutils.video import VideoStream
import numpy as numpy
import argparse
import cv2
import imutils
import time

ap = argparse.ArgumentParser()

ap.add_argument("-v", "--video",
    help="path to (optional) video file")
    
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")

args = vars(ap.parse_args())
greenLower = (29,86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
    vs = VideoStream(src=0).start()
else:
    vs = cv2.VideoCapture(args["video"])

time.sleep(2.0)