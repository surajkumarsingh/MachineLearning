import cv2

face_cascade = cv2.CascadeClassifier("cascade.xml")

img = cv2.imread("Jim.jpg")
print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
print(type(face))
print(face)

for x, y, w, h in face:

    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()