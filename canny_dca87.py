# canny.py
"""
Altered canny edge detector
Author: Dylan Carlyle
Date: 6/6/2019

Improved canny edge detector, better suited to detect edges on buildings.
"""
import cv2
import numpy as np

def nothing(x):
    # We need a callback for the createTrackbar function.
    # It doesn't need to do anything, however.
    pass


img = cv2.imread('./canny_images/1 (15).jpg', 0)

    
# Create a window and add two trackbars for controlling the thresholds.
cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Threshold1', 'Canny Edge Detection', 100, 1200, nothing)
cv2.createTrackbar('Threshold2', 'Canny Edge Detection', 200, 1200, nothing)

while True:
    # Get the latest threshold values.
    threshold1 = cv2.getTrackbarPos('Threshold1', 'Canny Edge Detection')
    threshold2 = cv2.getTrackbarPos('Threshold2', 'Canny Edge Detection')

    # Update the image using the latest threshold.
    edges = cv2.Canny(img, threshold1, threshold2)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.imwrite
    


    if cv2.waitKey(100) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
