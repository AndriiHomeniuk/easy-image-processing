import cv2
import sys


# Read the image. The first command line argument is the image
image = cv2.imread(sys.argv[1])

cv2.imshow("ImageStarWars", image)
cv2.waitKey(0)
