import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

face_cascade_path = os.path.join(script_dir, '..', 'cascades', 'haarcascade_frontalface_default.xml')
    
face_cascade = cv2.CascadeClassifier(face_cascade_path)
    

cap = cv2.VideoCapture(0)

while True:
   
    ret, frame = cap.read()
    if not ret:
        break

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
       
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    
    num_faces = len(faces)
    face_count_text = f"Faces Detected: {num_faces}"

    cv2.putText(frame, face_count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow('Webcam Feed - Face Counter', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or cv2.getWindowProperty('Webcam Feed - Face Counter', cv2.WND_PROP_VISIBLE) < 1:
        break


cap.release()
cv2.destroyAllWindows()
