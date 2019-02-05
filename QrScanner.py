from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
text = ''
# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it to
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)

        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Barcode Scanner", frame)
    cv2.waitKey(1) #& 0xFF == ord(' '):
    #If text contains Data Loop will break
    if text != "":
        break
print(text)
cv2.destroyAllWindows()
vs.stop()
