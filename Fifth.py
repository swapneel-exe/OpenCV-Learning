import cv2

img = cv2.imread('Image_Files/Image6.jpg')
cv2.imshow('Basic Image', img)
cv2.waitKey(0)

# Resizing an Image
# cv2.resize(Image_variable, size, interpolation)
resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized',resize)
cv2.waitKey(0)

# Cropping an Image
# img[x-start:x-end, y-start:y-end]
cropped = img[50:200,200:400]
cv2.imshow('Cropped',cropped)
cv2.waitKey(0)