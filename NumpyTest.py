import cv2

imgColor = cv2.imread("Jim.jpg", 1)
print(imgColor.shape)
print(type(imgColor))
imgBnW = cv2.imread("Jim.jpg", 0)
print(imgBnW.shape)
print(type(imgBnW))

img =cv2.imshow("JimColor", imgColor)
cv2.waitKey(0)

img =cv2.imshow("JimB&W", imgBnW)
cv2.waitKey(0)#Press any key to close windows
#cv2.waitKey(2000)#wait for 2000 milis  and destroy by cv2.destroyAllWindows()
#cv2.destroyAllWindows()