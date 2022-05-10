import cv2 as cv
import mediapipe as mp
import time

# Image source
cap = cv.VideoCapture(1)

# Hands mapping object
mpHands = mp.solutions.hands
hands = mpHands.Hands() # Only RGB img

while True:
    # Frame captured from camera
    succes, frame = cap.read()  

    # Convert image from BGR format to RGB format
    frameRgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frameRgb)

    print(results)

    # Show image
    cv.imshow("Frame", frame)
    cv.waitKey(1)