import numpy as np
import cv2

cap = cv2.VideoCapture(0)   # enable webcam

while(1):
    ret, frame = cap.read() # read frames
    cv2.imshow('The_Input_Frame', frame)    # display original img
    edges = cv2.Canny(frame, 100, 100)  # canny edge detection 
    cv2.imshow('Edges', edges)  # getting output as frame
    k = cv2.waitKey(5) & 0xFF
    if k == 27: # escape key
        break

# release camera
cap.release()