import numpy as np
import cv2

detector = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainingData.yml")
iD = 0
iDe = ""
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        iD, conf = rec.predict(gray[y:y+h, x:x+w])
        if(iD > 1):
            #iD = "Ashok Nanda Sir"
            print(iD)
            print(type(iD))
        #cv.putText(img, 'ID: ' + eid, (50, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
            iDe = str(iD)
    cv2.putText(img, 'ID: ' + iDe, (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', img)
    if (cv2.waitKey(1)== ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

