
from PIL import ImageGrab
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:

    img = ImageGrab.grab(bbox=(300,100,800,800))

    frame = np.array(img)   

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Frame", frame)

    key = cv.waitKey(1)

    if key == 27:
        break

cap.release()
cv.destroyAllWindows()

""" def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

if __name__ == "__main__":
    print(returnCameraIndexes()) """