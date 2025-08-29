import cv2
import mediapipe as mp
import math
import numpy as np
import platform

if platform.system() == "Windows":
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    vol_range_min, vol_range_max, _ = volume.GetVolumeRange() 

elif platform.system() == "Darwin": 
    import os
    vol_range_min, vol_range_max = 0, 100 

else: 
    print("not sutable os")
    exit()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Hand Gesture Volume Control is running. Pinch to change volume. Press 'q' to quit.")


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        h, w, c = img.shape
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
        x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 12, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        
        distance = math.hypot(x2 - x1, y2 - y1)
        
        vol_level = np.interp(distance, [20, 200], [vol_range_min, vol_range_max])
        
        vol_percent = np.interp(distance, [20, 200], [0, 100])
        
        vol_bar_height = np.interp(vol_percent, [0, 100], [400, 150])

        if platform.system() == "Windows":
            volume.SetMasterVolumeLevel(vol_level, None)
        elif platform.system() == "Darwin":
            os.system(f"osascript -e 'set volume output volume {int(vol_level)}'")
        
        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
        cv2.rectangle(img, (50, int(vol_bar_height)), (85, 400), (0, 0, 255), cv2.FILLED) 
        
        cv2.putText(img, f'{int(vol_percent)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Gesture Volume Control", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()