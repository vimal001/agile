import cv2
import sys

# Get user supplied values
imagePath = sys.argv[0]
cascPath = sys.argv[0]

# Create the haar cascade
face_cascade = cv2.CascadeClassifier('C:/Users/vimal/Downloads/opencv/FaceDetect-master/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/vimal/Downloads/opencv/FaceDetect-master/haarcascade_eye.xml')

# Read the image
image = cv2.imread('C:/Users/vimal\Downloads/opencv/FaceDetect-master/image1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.15, 2)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

print "Found {0} faces!".format(len(faces))
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
