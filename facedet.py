import cv2
from random import randrange

facedata = cv2.CascadeClassifier('C:\STD\Projects\python pro\Face.xml')
img=cv2.VideoCapture(0)

while True:
    yes,frame = img.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    

    face_cord = facedata.detectMultiScale(gray)
    for (x,y,w,h) in face_cord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),2)
    cv2.imshow("heyy",frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break


img.release()