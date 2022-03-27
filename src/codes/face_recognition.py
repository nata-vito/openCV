import cv2
from random import randrange

# 1
# Faces frontais pre-treinadas
trained_face_data = cv2.CascadeClassifier('..\data\haarcascade_frontalface_default.xml')

# Photo to detect face
#img = cv2.imread('..\img\women1.jpg', cv2.IMREAD_UNCHANGED)
faces_img = cv2.imread('..\img\\faces.jpg', cv2.IMREAD_UNCHANGED)

# 2
gray_img = cv2.cvtColor(faces_img, cv2.COLOR_BGR2GRAY)

# 3 - detect faces
face_coordinates = trained_face_data.detectMultiScale(gray_img) # return the coordinates from face

print(len(face_coordinates))

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(faces_img, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)


# Show img
cv2.imshow('Face recognition', faces_img)
cv2.waitKey()

print('ok')