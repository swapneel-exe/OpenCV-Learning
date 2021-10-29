# Importing Libraries
import cv2

# Importing Image File
img = cv2.imread('Image_Files/Image8.jpg')
cv2.imshow('Primary Image', img)
cv2.waitKey(0)

# Converting to Grayscale
# cv2.cvtColor(Image_Variable, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)

# Blurring the Image
# cv2.GaussianBlur(Image_Variable, Kernel_Size, Border_Type)
# Note: Kernel Size is always ina pair of odd numbers. Higher the number the greater is the blur.
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)

# Edge Cascading
# cv2.Canny(Image_Variable, Initial_Threshold, Final_Threshold)
canny = cv2.Canny(img, 125, 175)
cv2.imshow('Edge Cascading', canny)
cv2.waitKey(0)