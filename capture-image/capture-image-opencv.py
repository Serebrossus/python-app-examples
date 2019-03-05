# use OpenCV lib
from cv2 import *

# 0 - index of camera
cam = VideoCapture(0)
s, img = cam.read()

if s:
    # frame capture without any errors
    namedWindow('cam-test', WINDOW_AUTOSIZE)
    imshow('cam-test', img)
    waitKey(0)
    destroyWindow('cam-test')
    # save image
    imwrite('test-file.jpg', img)
