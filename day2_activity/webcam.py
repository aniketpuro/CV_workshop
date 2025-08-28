import cv2

# --- Setup ---
# Initialize the webcam. 0 is usually the default built-in webcam.
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# --- Main Loop ---
# This loop reads frames from the webcam continuously
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If a frame was not captured correctly, break the loop
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    # --- Image Transformations ---

    # 1. Flip: Flip the frame horizontally (1=horizontal, 0=vertical)
    flipped_frame = cv2.flip(frame, 1)

    # 2. Rotate: Rotate the frame 90 degrees clockwise
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # 3. Grayscale: Convert the frame from BGR to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. HSV: Convert the frame from BGR to HSV (Hue, Saturation, Value)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 5. BGR: The original frame is already in BGR format
    bgr_frame = frame

    # 6. Resize: Resize the frame to a width of 300 and height of 400
    resized_frame = cv2.resize(frame, (300, 400))


    # --- Display Windows ---
    # Show each transformed frame in its own window
    cv2.imshow('Original BGR', bgr_frame)
    cv2.imshow('Flipped', flipped_frame)
    cv2.imshow('Rotated 90 deg', rotated_frame)
    cv2.imshow('Grayscale', gray_frame)
    cv2.imshow('HSV', hsv_frame)
    cv2.imshow('Resized (300x400)', resized_frame)


    # --- Exit Condition ---
    # Press 'q' on the keyboard to exit the loop and close all windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
# When everything is done, release the capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()