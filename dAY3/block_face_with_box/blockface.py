import cv2
import os

# --- Build the absolute path to the cascade file ---
# The path now goes up two directories ('..', '..') to find the parallel 'cascades' folder.
script_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade_path = os.path.join(script_dir, '..', '..', 'cascades', 'haarcascade_frontalface_default.xml')

try:
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    if face_cascade.empty():
        raise cv2.error("Cascade file failed to load. Check the path.")
except cv2.error:
    print(f"Error: Could not load cascade file from path: {face_cascade_path}")
    print("Make sure the file exists and the path is correct relative to your script.")
    exit()

# Connect to the default webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting live feed. Press 'q' or click the 'X' to close.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for the detector
    # --- FIXED THIS LINE ---
    # Corrected the typo from COLOR_BGR_GRAY to COLOR_BGR2GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.putText(frame, 'LIVE', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    # Loop through each face found
    for (x, y, w, h) in faces:
        # --- Replace the face with a red rectangle ---
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), -1)

    # Display the final frame
    cv2.imshow('Webcam Feed - Face Blocker', frame)

    # Check for user input to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or cv2.getWindowProperty('Webcam Feed - Face Blocker', cv2.WND_PROP_VISIBLE) < 1:
        break