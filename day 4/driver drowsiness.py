import cv2
import os
import time
import winsound

ASSUMED_FPS = 30.0
EYE_CLOSED_FRAMES_THRESHOLD = int(ASSUMED_FPS * 5)
NO_FACE_TIME_THRESHOLD = 5.0

script_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade_path = os.path.join(script_dir, '..', 'cascades', 'haarcascade_frontalface_default.xml')
eye_cascade_path = os.path.join(script_dir, '..', 'cascades', 'haarcascade_eye.xml')

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

if face_cascade.empty() or eye_cascade.empty():
    print("Error loading cascade files.")
    exit()

cap = cv2.VideoCapture(0)

drowsy_counter = 0
no_face_start_time = None
alarm_on = False
status_text = "Initializing..."

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8, minSize=(80, 80))

    if len(faces) > 0:
        no_face_start_time = None
        (x, y, w, h) = faces[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        eye_roi_y_start = y
        eye_roi_y_end = y + int(h * 0.6)
        eye_roi_gray = gray[eye_roi_y_start:eye_roi_y_end, x:x+w]

        eyes = eye_cascade.detectMultiScale(eye_roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(30, 30))

        if len(eyes) >= 2:
            status_text = "Status: Active"
            drowsy_counter = 0
            alarm_on = False
        else:
            drowsy_counter += 1
            status_text = "Status: Inactive"

            if drowsy_counter >= EYE_CLOSED_FRAMES_THRESHOLD:
                alarm_on = True
                status_text = "DROWSINESS ALERT!"

            if drowsy_counter > 0:
                frames_left = EYE_CLOSED_FRAMES_THRESHOLD - drowsy_counter
                seconds_left = max(0, frames_left / ASSUMED_FPS)
                timer_text = f"ALARM IN: {seconds_left:.1f}s"
                
                (text_width, text_height), _ = cv2.getTextSize(timer_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                text_x = (width - text_width) // 2
                text_y = height - 30
                
                cv2.putText(frame, timer_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    else:
        status_text = "NO DRIVER DETECTED!"
        if no_face_start_time is None:
            no_face_start_time = time.time()
        
        elapsed_no_face = time.time() - no_face_start_time
        
        if elapsed_no_face > NO_FACE_TIME_THRESHOLD:
            alarm_on = True
            
    cv2.putText(frame, status_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if alarm_on:
        cv2.rectangle(frame, (0, 0), (width-1, height-1), (0, 0, 255), 10)
        winsound.Beep(500, 700)

    cv2.imshow("Accurate Drowsiness Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()