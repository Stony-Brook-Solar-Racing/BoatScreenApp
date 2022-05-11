import numpy as np
import cv2

cap = cv2.VideoCapture(1)   # enable webcam

while(1):
    _, image = cap.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_range = np.array([0,100,100])
    upper_range = np.array([5,255,255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    edges = cv2.Canny(image, 100, 70)
    cv2.imshow('normal_window', image)
    cv2.imshow('red tape', mask)
    cv2.imshow('edges', edges)
    k = cv2.waitKey(5)

# release camera
cap.release()