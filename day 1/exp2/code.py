import cv2

# Define the input and output filenames with different extensions
input_filename = 'sample_image.png'
output_filename_jpg = 'converted_image.jpg'

# Read the original image
img = cv2.imread(input_filename)

if img is None:
    print(f"Error: Could not read the image at {input_filename}")
else:
    # Save the image with a .jpg extension
    # OpenCV automatically handles the conversion from PNG to JPEG
    cv2.imwrite(output_filename_jpg, img)
    print(f"Image converted and saved as '{output_filename_jpg}'.")