from imutils.video import VideoStream
import cv2

# grab reference to webcam
vs = VideoStream(src=0).start()
while True:
    # grab current frame
    frame = vs.read()

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        break

    # show frame to our screen
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    if key  == ord('q'):
        break

# close all windows
cv2.destroyAllWindows()
