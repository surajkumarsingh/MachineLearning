import cv2 as cv
import winsound
import pandas as pd
from _datetime import datetime
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time


class QRScannerAndSmile:
    @staticmethod
    def qr():
        # initialize the video stream and allow the camera sensor to warm up
        global text, eid, name
        vs = VideoStream(src=0).start()
        time.sleep(2.0)
        text = ''
        # loop over the frames from the video stream
        while True:
            # grab the frame from the threaded video stream and resize it to
            frame = vs.read()
            frame = imutils.resize(frame, width=600)
            # find the QrCodes in the frame and decode each of the barcodes
            QrCodes = pyzbar.decode(frame)
            cv.putText(frame, 'SHOW QR CODE', (200, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
            # loop over the detected QRcodes
            for QrCode in QrCodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = QrCode.rect
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                qrcodeData = QrCode.data.decode("utf-8")
                # qrcodeData = QrCode.type
                # show QrCode data
                text = "{}".format(qrcodeData)
                cv.putText(frame, text, (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv.imshow("QR Code Scanner", frame)
            # if cv.waitKey(1) & 0xFF == ord(' '):
            # If text contains Data Loop will break
            if cv.waitKey(1) and text != "":
                winsound.PlaySound("C:\\Users\\suraj_kumar\\PycharmProjects\\Demo\\camera-shutter.wav",
                                   winsound.SND_ASYNC | winsound.SND_ALIAS)
                break
        # print(text)
        name = text.split('\n')[0]
        eid = text.split('\n')[1]
        print(name + " " + eid)
        cv.destroyWindow("QR Code Scanner")
        vs.stop()

    @staticmethod
    def faceandsmile():
        Id = eid
        # print("in smile")
        # print(Id)
        face_classifier = cv.CascadeClassifier('C:\\Users\\suraj_kumar\\PycharmProjects\\Demo\\face_cascade.xml')
        smile_classifier = cv.CascadeClassifier('C:\\Users\\suraj_kumar\\PycharmProjects\\Demo\\Haar_smile.xml')
        times = []
        smile_ratios = []
        sm_ratio = 0
        cap = cv.VideoCapture(0)

        while True:
            ret, img = cap.read()
            # ret2, img2 = cap.read()
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = cv.GaussianBlur(gray, (21, 21), 0)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                roi_gray = gray[y:y + h, x:x + w]
                roi_img = img[y:y + h, x:x + w]
                cv.putText(img, 'Name: ' + name, (300, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                cv.putText(img, 'ID: ' + eid, (50, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                smile = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                          minNeighbors=22,
                                                          minSize=(25, 25))
                # print("Found {0} faces!".format(len(faces)))

                for (sx, sy, sw, sh) in smile:
                    cv.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
                    sm_ratio = str(round(sw / sx, 2))
                    font = cv.FONT_HERSHEY_SIMPLEX
                    cv.putText(img, 'Smile Scale : ' + sm_ratio, (10, 50), font, 1, (200, 255, 155), 2, cv.LINE_AA)
                    if float(sm_ratio) > 2.50:
                        sm_ratio = float(sm_ratio)
                        cv.imwrite('C:/Users/suraj_kumar/Pictures/Saved Pictures/' + Id + '.jpg', img)
            cv.imshow('Face And Smile Detector', img)
            if cv.waitKey(1) & 0xFF == ord(' '):
                break
        smile_ratios.append(float(sm_ratio))
        times.append(datetime.now())
        ds = {'ID': Id, 'Smile_Score': smile_ratios, 'Time': times}
        df = pd.DataFrame(ds)
        with open('smile_records.csv', 'a') as csvFile:
            df.to_csv(csvFile, header=False, index=False)
        csvFile.close()
        cv.destroyAllWindows()
        cap.release()

    def call(self):
        QRScannerAndSmile.qr()
        QRScannerAndSmile.faceandsmile()

#obj = QRScannerAndSmile()
#obj.call()



