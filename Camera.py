import cv2, time

video = cv2.VideoCapture(0)
print(video)
#frame is Numpy aaray, it represents the first image that
#video captures "check" it is data type, returns if python is able to read the VideoCapture object
check, frame = video.read()
print(check)
print(frame)
time.sleep(3)
#used to capture first image/frame of the video
cv2.imshow("capture", frame)
cv2.imwrite('jpg.jpg', frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()