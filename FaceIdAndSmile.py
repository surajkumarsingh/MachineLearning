import cv2 as cv
import winsound
from _datetime import datetime
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
from MysqlConnection import insertdata


class QRScannerAndSmile:
    @staticmethod
    def qr():
        # initialize the video stream and allow the camera sensor to warm up
        global text, eid, name
        vs = VideoStream(src=0).start()
        #vs =cv.VideoCapture(0)
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
                winsound.PlaySound("camera-shutter.wav",
                                   winsound.SND_ASYNC | winsound.SND_ALIAS)
                break
        # print(text)
        name = text.split('\n')[0]
        eid = text.split('\n')[1]
        print(name + " " + eid)
        cv.destroyWindow("QR Code Scanner")
        #vs.release()
        vs.stop()

    @staticmethod
    def faceandsmile():
        print("in Face and smile")
        print(eid)
        i = 0
        # Set the font style
        font = cv.FONT_HERSHEY_SIMPLEX
        # Create Local Binary Patterns Histograms for face Recognition
        recognizer = cv.face.LBPHFaceRecognizer_create()

        # Load the trained mode
        recognizer.read('YmlFiles/trainer.yml')


        face_classifier = cv.CascadeClassifier('cascade.xml')
        smile_classifier = cv.CascadeClassifier('Haar_smile.xml')
        # smile_ratios = 0
        # sm_ratio = 0
        cap = cv.VideoCapture(0)

        while True:
            ret, img = cap.read()
            # ret2, img2 = cap.read()
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            #gray = cv.GaussianBlur(gray, (21, 21), 0)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                roi_gray = gray[y:y + h, x:x + w]
                roi_img = img[y:y + h, x:x + w]
                # Recognize the face belongs to which ID
                Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                prediction = round(100 - confidence, 2)
                #print(prediction)
                #print(type(prediction))
                if float(prediction) > 60.55:
                    percentage = "{0:.2f}%".format(round(100 - confidence, 2))
                    # print(type(Id))
                    # Put text describe who is in the picture
                    cv.putText(img, percentage, (x, y - 40), font, 1, (255, 255, 255), 3)
                    cv.putText(img, 'Name:' + name, (300, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                    cv.putText(img, 'ID:' + eid, (50, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                    smile = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                          minNeighbors=22,
                                                          minSize=(25, 25))
                    for (sx, sy, sw, sh) in smile:
                        cv.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
                        sm_ratio = str(round(sw / sx, 2))
                        font = cv.FONT_HERSHEY_SIMPLEX
                        cv.putText(img, 'Smile Scale : ' + sm_ratio, (10, 50), font, 1, (200, 255, 155), 2, cv.LINE_AA)
                        if float(sm_ratio) > 2.50:
                            smile_ratios = sm_ratio
                            print(smile_ratios)
                            # door = cv.VideoCapture("door-open.gif")
                            # b, d = door.read()
                            # cv.imshow("door open", d)
                            i = 2
                            if cv.waitKey(1) & i == 2:  # if float(sm_ratio) > 2.50: #0xFF == ord(' '):
                                break
                                # smile_ratios = sm_ratio
                                cv.imwrite('C:/Users/suraj_kumar/Pictures/Saved Pictures/' + eid + '.jpg', img)
                                # print(name)
                                print(smile_ratios)
                                times = datetime.now()
                                times = times.replace(microsecond=0)
                                insertdata(eid, name, smile_ratios, times, 'C:/Users/suraj_kumar/Pictures/Saved Pictures/' + eid + '.jpg')

                                cv.destroyAllWindows()
                                cap.release()

                # print("Found {0} faces!".format(len(faces)))

                         #cv.imwrite('C:/Users/suraj_kumar/Pictures/Saved Pictures/' + eid + '.jpg', img)
            cv.imshow('Face And Smile Detector', img)


    def call(self):
        QRScannerAndSmile.qr()
        QRScannerAndSmile.faceandsmile()


obj = QRScannerAndSmile()
obj.call()