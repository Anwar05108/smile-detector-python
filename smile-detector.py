import cv2
# import numpy

face_detector = cv2.CascadeClassifier('haarrcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
webcam = cv2.VideoCapture(0)

while True:

    (successful_frame_read, frame) = webcam.read()

    if not successful_frame_read:
        break
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_grayscale)
    

    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        the_face = frame[y:y+h, x:x+w]
        # the_face = (x, y, w, h)

        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)


        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7
        , minNeighbors=20)


        for (x, y, w, h) in smiles:
            cv2.rectangle(the_face, (x, y), (x+w, y+h), (50, 50, 200), 4)

        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (50, 50, 200), 4)


            if len(smiles) > 0:
                cv2.putText(frame, 'smiling'
                ,(x, y+h+40), fontScale=3,
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                color=(255,255,255))
        




    cv2.imshow('Smile Detector', frame)

    # print(faces)

    cv2.waitKey(1)

webcam.release()
cv2.destroyAllWindows()

