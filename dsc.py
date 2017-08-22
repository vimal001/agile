Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 5, in <module>
    imagePath = sys.argv[1]
IndexError: list index out of range
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 6, in <module>
    cascPath = sys.argv[2]
IndexError: list index out of range
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 6, in <module>
    cascPath = sys.argv[1]
IndexError: list index out of range
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 9, in <module>
    faceCascade = cv2.CascadeClassifier(cascPath)
error: C:\builds\master_PackSlaveAddon-win64-vc12-static\opencv\modules\core\src\persistence.cpp:2220: error: (-212) C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py(1): Valid XML should start with '<?xml ...?>' in function icvXMLParse

>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 13, in <module>
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
error: C:\builds\master_PackSlaveAddon-win64-vc12-static\opencv\modules\imgproc\src\color.cpp:7564: error: (-215) scn == 3 || scn == 4 in function cv::cvtColor

>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 3 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 1 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 17, in <module>
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
NameError: name 'face_cascade' is not defined
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 17, in <module>
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
NameError: name 'face_cascade' is not defined
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 19, in <module>
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
NameError: name 'img' is not defined
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 7 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 16, in <module>
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
NameError: name 'face_cascade' is not defined
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =

Traceback (most recent call last):
  File "C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py", line 21, in <module>
    eyes = eye_cascade.detectMultiScale(roi_gray)
NameError: name 'eye_cascade' is not defined
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 3 faces!

= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 1 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 7 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 6 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 6 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 5 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 5 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 5 faces!
>>> 
= RESTART: C:\Users\vimal\Downloads\opencv\FaceDetect-master\face_detect.py =
Found 4 faces!
