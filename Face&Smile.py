import cv2 as cv
import pandas as pd
from _datetime import datetime
from BarCodeScanner import BarAndQR
#from  BarAndQR import text


class FaceAndSmile(BarAndQR):
    def run(self):
        d = BarAndQR()
        d.Bar()
        BarAndQR.text
        Id = input('Enter Id:-'+d.text)
        print(Id)
        face_classifier = cv.CascadeClassifier('cascade.xml')
        smile_classifier = cv.CascadeClassifier('Haar_smile.xml')
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
                smile = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                          minNeighbors=22,
                                                          minSize=(25, 25))
                # print("Found {0} faces!".format(len(faces)))

                for (sx, sy, sw, sh) in smile:
                    cv.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
                    sm_ratio = str(round(sw / sx, 2))
                    font = cv.FONT_HERSHEY_SIMPLEX
                    cv.putText(img, 'Smile meter : ' + sm_ratio, (10, 50), font, 1, (200, 255, 155), 2, cv.LINE_AA)
                    if float(sm_ratio) > 2.50:
                        sm_ratio = float(sm_ratio)
                        cv.imwrite('C:/Users/suraj_kumar/Pictures/Saved Pictures/' + Id + '.jpg', img)
            cv.imshow('Smile Detector', img)
            if cv.waitKey(1) & 0xFF == ord(' '):
                break
        smile_ratios.append(float(sm_ratio))
        times.append(datetime.now())
        ds = {'ID': Id, 'Smile_Score': smile_ratios, 'Time': times}
        df = pd.DataFrame(ds)
        with open('smile_records.csv', 'a') as csvFile:
            df.to_csv(csvFile, header=False, index=False)
        csvFile.close()
        cap.release()
        cv.destroyAllWindows()
s = FaceAndSmile()
s.run()
