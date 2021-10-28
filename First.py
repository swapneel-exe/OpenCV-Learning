# Importing Libraries
import cv2
import numpy as np

# Loading an Image File
img = cv2.imread('Image_Files/Image1.jpg')

# Displaying the loaded Image File
cv2.imshow('Moon Image', img)

# waitkey() -> allows users to display a window for given milliseconds or until any key is pressed.
# 0 -> Display until any key is pressed
cv2.waitKey(0)