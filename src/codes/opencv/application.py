from PIL import ImageGrab
import cv2 as cv
import time
import os
import numpy as np
import hand_tracking as ht
from api_request import FireRise

# Camera capture
cap         = cv.VideoCapture(1)
i           = 0
tracking    = ht.handDetector(detectionCon=0.75)    
ids         = [4, 8, 12, 16, 20]

""" if(cap.isOpened() == False):
    print("Error openning the video")
else: 
    # Frame rate info
    fps = cap.get(5)
    print('Frames per second: ', fps, 'FPS')

    # Frame count
    frame_count = cap.get(7)
    print('Frame Count: ', frame_count) """


while True:
    ret, frame  = cap.read()
    #img = ImageGrab.grab(bbox=(300,100,800,800))
    frame = np.array(frame)   
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    contour     = tracking.findHands(frame)
    pose        = tracking.findPosition(frame)
    i          += 1
    

    if len(pose) != 0:
        fingers = []
        
        print(tracking.label)

        if tracking.label == 'Left':
            # hand Thumb -> Left
            if pose[ids[0]][1] > pose[ids[0] - 1][1]:
                    fingers.append(1)
            else: 
                fingers.append(0)

        elif tracking.label == 'Right':
            # hand Thumb -> Right
            if pose[ids[0]][1] < pose[ids[0] - 1][1]:
                    fingers.append(1)
            else: 
                fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            # Check finger reference points to define hand is openq or not
            if pose[ids[id]][2] < pose[ids[id] - 2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
        
        print(fingers)
        api = FireRise("https://myhand-ff333-default-rtdb.firebaseio.com/", fingers)
        api.putData("mao", True, None, fingers)

        cv.imshow('Frame', frame)
        key = cv.waitKey(20)

        if key == ord('q'):
            break


    """ if ret:
        cv.imshow('Frame', frame)
        key = cv.waitKey(20)

        if key == ord('q'):
            break
    else:
        break """

#cap.release()
cv.destroyAllWindows()