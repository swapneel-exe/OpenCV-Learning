# Importing Libraries
import cv2

# Function to Resize the Frame (Universal)
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

# Function to Read and Show a Video File
capture = cv2.VideoCapture('Video_Files/Video1.mp4')
while True:
    isTrue, frame =  capture.read()
    frame_res = rescaleFrame(frame, scale=0.25)
    cv2.imshow('Video',frame)
    # Condition for Closing the Window Frame i.e. Automatically after 20 ms or press 'w'
    if cv2.waitKey(20) & 0xFF==ord('w'):
        break
    # Rescaling the Video Frame
    cv2.imshow('Video Rescaled',frame_res)
    # Condition for Closing the Window Frame i.e. Automatically after 20 ms or press 'q'
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

# Function to Read and Show a Webcam
# 0 -> Default Webcam and use subsequent numbers to read other available Webcams
live = cv2.VideoCapture(0)

while True:
    isTrue, frame =  live.read()
    cv2.imshow('Video',frame)
    # Condition for Closing the Window Frame i.e. Automatically after 20 ms or press 'x'
    if cv2.waitKey(20) & 0xFF==ord('x'):
        break
live.release()
cv2.destroyAllWindows() 