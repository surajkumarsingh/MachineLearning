import cv2, time

first_frame = none

video = cv2.VideoCapture(0)

while true:

    check, frame = video()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

delta_frame = cv2.absdiff(first_frame,gray)
thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY[1])
thresh_delta = cv2.dilate(thresh_delta, None, Iterations=0)
(_,cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)

for contour in cnts:
    if cv2.contourArea((contour) < 1000:
continue
(x, y, w, h) = cv2.boundingRect(contour)
cv2.rectagle(frame, (x,y), (x+W, y+h), (0,255,0),3)

cv2.imshow('frame', frame)
cv2.imshow('capturing',gray)
cv2.imshow('delta',delta_frame)

key = cv2.waitKey(1)
if key == ord('q'):
    break
video.release()
cv2.destroyAllWindows()