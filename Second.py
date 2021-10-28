# Importing Libraries
import cv2
import numpy as np

# Initialising a Blank Screen
blank = np.zeros((480,640,3), dtype = 'uint8') # (height, width, depth)
blank[:] = 255,0,0 # OpenCV follows BGR format

cv2.imshow('Blank Screen Painted Blue', blank)
cv2.waitKey(0)

# Draw a Line
#cv2.line(Drawing_Screen, Starting_Point, Ending_Point, Colour, Thickness)
cv2.line(blank,(blank.shape[1]//2,blank.shape[0]//2),(blank.shape[1], blank.shape[0]),(255,255,255),thickness=20)
cv2.imshow('Line',blank)
cv2.waitKey(0)

# Drawing a Rectangle
# cv2.rectangle(Drawing_Screen, Starting_Point, Ending_Point, Colour, Thickness)
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = cv2.FILLED) # (blank.shape[0]//2, blank.shape[1]//2) -> returns mid point
cv2.imshow('Rectangle', blank)
cv2.waitKey(0)

# Draw a Circle
# cv2.circle(Drawing_Screen, Center, Radius, Color, Thickness)
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(0,0,255),thickness=-1)
cv2.imshow('Circle',blank)
cv2.waitKey(0)

# Writing Text
#cv2.putText(Drawing_Screen, 'Input_text', Position, Font_Face, Font_Scale, Color, Thickness)
cv2.putText(blank,'Hello!! This is Swapneel !!',(30,400),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,0,0),2)
cv2.imshow('Text',blank)
cv2.waitKey(0)


