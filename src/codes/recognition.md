### First Steps:
-> Get a Crap-Load of Faces
-> Turn pictures to black and white
-> Train the algorithm to detect faces

-> Install openCV ( pip install opencv-python opencv-python-headless)

-> haarcascade_frontalface_default.xml (data trainned)

-> Criar retangulo

cv.rectangle(	img, pt1, pt2, color[, thickness[, lineType[, shift]]]	) ->	img

Parameters
img	- Image.
pt1	- Vertex of the rectangle.
pt2	- Vertex of the rectangle opposite to pt1 .
color - Rectangle color or brightness (grayscale image).
thickness - Thickness of lines that make up the rectangle. Negative values, like FILLED, mean that the function has to draw a filled rectangle.
lineType - Type of the line. See LineTypes
shift - Number of fractional bits in the point coordinates.

cv2.rectangle(img, (face_coordinates[0][0], face_coordinates[0][1]), 
             (face_coordinates[0][2] + face_coordinates[0][0], 
             face_coordinates[0][3] + face_coordinates[0][1]), (0, 255, 0), 2)