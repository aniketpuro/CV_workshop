import cv2
import os
import datetime


def create_slow_motion_video(original_filepath):
    """
    Creates slow motion version from high frame rate video
    """
    try:
        # Read original video
        cap = cv2.VideoCapture(original_filepath)
        if not cap.isOpened():
            print("Error: Could not open original video file.")
            return
        
        # Get video information
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Create slow motion file name
        base_name = os.path.splitext(original_filepath)[0]
        slow_motion_filepath = f"{base_name}_slow.MP4"
        
        # Create slow motion video writer (with lower frame rate)
        slow_fps = original_fps / SLOW_MOTION_FACTOR
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(slow_motion_filepath, fourcc, slow_fps, (frame_width, frame_height))
        
        print(f"Creating slow motion video: {slow_motion_filepath}")
        print(f"Original FPS: {original_fps:.1f} → Slow Motion FPS: {slow_fps:.1f}")
        
        # Copy all frames
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            frame_count += 1
        
        cap.release()
        out.release()
        
        print(f"Slow motion video ready! Total {frame_count} frames processed.")
        print(f"Original file: {original_filepath}")
        print(f"Slow motion file: {slow_motion_filepath}")
        
    except Exception as e:
        print(f"Error creating slow motion video: {e}")

# ===================================================================
# >> Enter your IP Webcam IP address here <<
# This address appears in the IP Webcam app. Make sure to add '/video' at the end.
url = "http://10.191.228.6:8080/video"
# ===================================================================

# Folder where videos will be saved
save_folder = "save"

# If 'save' folder doesn't exist, create it
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
    print(f"'{save_folder}' folder has been created.")

# Connect to video stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not connect to video stream.")
    exit()

# Get video resolution
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Recording settings
NORMAL_FPS = 30.0  # Normal playback frame rate
RECORD_FPS = 2.0  # High frame rate recording (for slow motion)
SLOW_MOTION_FACTOR = 2.0  # Slow down factor (2x = half speed)

# Recording status and video writer object
is_recording = False
out = None

print("Camera is ready.")
print("Press 's' to start recording.")
print("Press 'q' to stop recording and exit.")
print(f"Recording at {RECORD_FPS} FPS for slow motion.")
print(f"Playback will be {SLOW_MOTION_FACTOR}x slower.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Stream disconnected, no frames received.")
        break

    # Wait for keyboard input
    key = cv2.waitKey(1) & 0xFF

    # If 's' is pressed and recording is not active
    if key == ord('s') and not is_recording:
        is_recording = True
        # Create filename based on current time
        now = datetime.datetime.now()
        filename = f"rec_slowmo_{now.strftime('%Y-%m-%d_%H-%M-%S')}.MP4"
        filepath = os.path.join(save_folder, filename)
        
        # Create video writer object (with high frame rate)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filepath, fourcc, RECORD_FPS, (frame_width, frame_height))
        print(f"[REC] Slow motion recording started... saving to '{filepath}' at {RECORD_FPS} FPS.")

    

    # If 'q' is pressed
    if key == ord('q'):
        if is_recording:
            print(f"[STOP] Recording stopped.")
            # Create slow motion version
            create_slow_motion_video(filepath)
        break

    # If recording is active, show status on frame and write to file
    if is_recording:
        # Show 'SLOW MOTION RECORDING' text on frame
        cv2.putText(frame, 'SLOW MOTION REC', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'{RECORD_FPS:.0f} FPS', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        out.write(frame)
    else:
        # Show 'LIVE' text on frame
        cv2.putText(frame, 'LIVE', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Press S for SlowMo', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show video window
    cv2.imshow('IP Webcam Feed', frame)

# Release all resources
if is_recording:
    out.release() # If recording was active, properly close the file
cap.release()
cv2.destroyAllWindows()
print("Program closed.")