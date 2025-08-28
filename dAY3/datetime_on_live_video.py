import cv2
import datetime


cap = cv2.VideoCapture(0)

cv2.namedWindow('Webcam Feed')

while True:
  
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time into a string like "YYYY-MM-DD HH:MM:SS"
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

    cv2.putText(frame, timestamp_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)


    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    if cv2.getWindowProperty('Webcam Feed', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()

cv2.destroyAllWindows()

print("Webcam feed closed.")
