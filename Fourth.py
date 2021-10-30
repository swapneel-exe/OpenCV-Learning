# Importing OpenCV Library
import cv2

# Importing Image File
img = cv2.imread('Image_Files/Image3.jpg')
cv2.imshow('Primary Image', img)
cv2.waitKey(0)

#To observe next two function we will be using Edge Cascaded Image
canny = cv2.Canny(img, 100, 175)
cv2.imshow('Edge Cascaded Image', canny)
cv2.waitKey(0)

# Dilating the Image
# cv2.dilate(Image_Variable, kernel_size, iterations)
dilate = cv2.dilate(canny, (5,5), iterations = 3)
cv2.imshow('Dilated Image', dilate)
cv2.waitKey(0)

# Eroding the Image
# cv2.erode(Image_Variable, kernel_size, iterations)
eroded = cv2.erode(dilate,(3,3),iterations=3)
cv2.imshow('Eroded Image',eroded)
cv2.waitKey(0)