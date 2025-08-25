import cv2

# Define the input and output filenames
input_filename = 'sample_image.png'
output_filename = 'output_image.png'

# 1. Read the image from the disk
# The function cv2.imread() returns a NumPy array representing the image
img = cv2.imread(input_filename)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Could not read the image at {input_filename}")
else:
    print("Image read successfully.")
    
    # 2. Display the image in a window
    # cv2.imshow() takes the window name and the image to display
    cv2.imshow('My Image Window', img)
    print("Displaying image. Press any key to close the window.")
    
    # cv2.waitKey(0) waits indefinitely for a key press
    # This is crucial to keep the window open until you're ready
    cv2.waitKey(0)
    
    # cv2.destroyAllWindows() closes all OpenCV windows
    cv2.destroyAllWindows()
    
    # 3. Write the image to the disk
    # cv2.imwrite() saves the image to the specified path
    cv2.imwrite(output_filename, img)
    print(f"Image successfully saved as '{output_filename}'.")