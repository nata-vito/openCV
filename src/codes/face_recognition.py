import cv2
from random import randrange

# 1
# Faces frontais pre-treinadas
trained_face_data = cv2.CascadeClassifier('..\data\haarcascade_frontalface_default.xml')

# To capture video from webcam
web_cam = cv2.VideoCapture(1)

# Show video
while True:

    # Read the current frame
    successful_frame_read, frame = web_cam.read()

    # Convert frame by frame to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3 - detect faces
    face_coordinates = trained_face_data.detectMultiScale(gray_img) # return the coordinates from face

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)

    cv2.imshow('Me', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

web_cam.release()


"""  
# Photo to detect face

# 1
# Faces frontais pre-treinadas
trained_face_data = cv2.CascadeClassifier('..\data\haarcascade_frontalface_default.xml')

#img = cv2.imread('..\img\women1.jpg', cv2.IMREAD_UNCHANGED)
#faces_img = cv2.imread('..\img\\faces.jpg', cv2.IMREAD_UNCHANGED)

# 2
gray_img = cv2.cvtColor(web_cam, cv2.COLOR_BGR2GRAY)


print(len(face_coordinates))

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(web_cam, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)


# Show img
cv2.imshow('Face recognition', web_cam)
cv2.waitKey()

print('ok') """