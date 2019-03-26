import cv2
import os


def assure_path_exists(path):
    dir = os.path.join(path, face_id)
    if not os.path.exists(dir):
        os.makedirs(dir)


# Start capturing video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('cascade.xml')

# For each person, one face id
face_id = input("Enter Employee Id: ")

# Initialize sample face image
count = 0

assure_path_exists("C:/Users/suraj_kumar/Pictures/dataSet")

# Start looping
while (True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x, y, w, h) in faces:
        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("C:/Users/suraj_kumar/Pictures/dataSet/"+face_id+ "/"+str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'SPACE' for at least 10ms
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

    # If image taken reach 100, stop taking pics
    elif count > 100:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()