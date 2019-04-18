import cv2 as cv
import os
import numpy as np
from PIL import Image


class SampleTakerAndYmlCreator:

    @staticmethod
    def sample_taker():
        global face_id

        def assure_path_exists(path):
            dir = os.path.join(path, face_id)
            if not os.path.exists(dir):
                os.makedirs(dir)

        # For each person, one face id
        face_id = input("Enter Employee Id: ")
        # path of DataSet Images
        assure_path_exists("C:/Users/suraj_kumar/Pictures/dataSet")

        # Start capturing video
        cam = cv.VideoCapture(0)

        # Detect object in video stream using Haarcascade Frontal Face
        face_detector = cv.CascadeClassifier('cascade.xml')

        count = 0
        # Start looping
        while True:

            # Capture video frame
            b, image_frame = cam.read()

            # Convert Image frame to gray scale
            gray = cv.cvtColor(image_frame, cv.COLOR_BGR2GRAY)

            # Detect frames of different sizes, list of faces rectangles
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            # Loops for each faces
            for (x, y, w, h) in faces:
                # Crop the image frame into rectangle
                cv.rectangle(image_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Increment sample face image
                count += 1
                # Save the captured image into the dataset folder
                cv.imwrite(
                    "C:/Users/suraj_kumar/Pictures/dataSet/" + face_id + "/" + str(face_id) + '.' + str(count) + ".jpg",
                    gray[y:y + h, x:x + w])
                # Display the video frame, with bounded rectangle on the person's face
                cv.imshow('frame', image_frame)
            # To stop taking video, press 'SPACE' for at least 100ms
            if cv.waitKey(100) & 0xFF == ord(' '):
                break
            # If image taken reach 120, stop taking pics
            elif count > 25:
                break
        # Stop video
        cam.release()
        # Close all started windows
        cv.destroyAllWindows()

    @staticmethod
    def yml_creator():

        # Create Local Binary Patterns Histograms for face recognization
        recognizer = cv.face.LBPHFaceRecognizer_create()

        # Using prebuilt frontal face training model, for face detection
        detector = cv.CascadeClassifier("cascade.xml")

        # Create method to get the images and label data
        def getImagesAndLabels(path):

            # Get all file path
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

            # Initialize empty face sample
            faceSamples = []

            # Initialize empty id
            ids = []

            # Loop all the file path
            for imagePath in imagePaths:

                # Get the image and convert it to grayscale
                PIL_img = Image.open(imagePath).convert('L')

                # PIL image to numpy array
                img_numpy = np.array(PIL_img, 'uint8')

                # Get the image id
                id = int(os.path.split(imagePath)[-1].split(".")[1])

                # Get the face from the training images
                faces = detector.detectMultiScale(img_numpy)

                # Loop for each face, append to their respective ID
                for (x, y, w, h) in faces:
                    # Add the image to face samples
                    faceSamples.append(img_numpy[y:y + h, x:x + w])

                    # Add the ID to IDs
                    ids.append(id)

            # Pass the face array and IDs array
            return faceSamples, ids

        # Get the faces and IDs
        print(face_id)
        faces, ids = getImagesAndLabels('C:/Users/suraj_kumar/Pictures/dataSet/'+face_id)

        # Train the model using the faces and IDs
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer.yml
        recognizer.save('YmlFiles/'+face_id+'.yml')


SampleTakerAndYmlCreator.sample_taker()
SampleTakerAndYmlCreator.yml_creator()
