# !/usr/bin/python
import cv2
import sys
import numpy as np

if len(sys.argv) < 2:
    video_capture = cv2.VideoCapture(0)
else:
    video_capture = cv2.VideoCapture(sys.argv[1])

# Read two frames, last and current, and convert current to gray.
ret, current_frame = video_capture.read()
while True:
    # We want two frames- last and current, so that we can calculate the different between them.
    # Store the current frame as last_frame, and then read a new one
    last_frame = current_frame
    ret, current_frame = video_capture.read()

    # Find the absolute difference between frames
    diff = cv2.absdiff(last_frame, current_frame)
    # If difference is greater than a threshold, that means motion detected.
    if np.mean(diff) > 10:
        print("Achtung! Motion detected.")

    # Display the resulting frame
    cv2.imshow('Video', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
