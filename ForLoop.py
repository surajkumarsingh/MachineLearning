import cv2
faces =["Jim.jpg","sattu.jpg"]
for f in faces:
    print(f)
    print(type(f))
    print(faces)
    img=cv2.imread('f',1)
  img =cv2.imshow("img",img)
cv2.waitKey(0)
