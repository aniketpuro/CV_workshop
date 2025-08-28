import cv2
import numpy as np

# Define the image dimensions (height, width)
height = 600
width = 800

# --- Create a blank white image ---
# We create a numpy array of the desired size filled with 1s,
# then multiply by 255 to get the color white (255, 255, 255).
# The data type is 'uint8' which is standard for images.
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

# --- 1. Draw a Circle ---
# Define circle properties
center_coordinates = (width // 2, height // 2) # Center of the image
radius = 100
circle_color = (255, 0, 0)  # BGR color for Blue
thickness = 3  # Use -1 for a filled circle

# Draw the circle on the white image
cv2.circle(white_image, center_coordinates, radius, circle_color, thickness)


# --- 2. Draw a Triangle ---
# A triangle is a polygon, so we define its three corner points (vertices).
pts = np.array([[400, 450], [650, 450], [525, 250]], np.int32)
# Reshape the points array to the format required by polylines
pts = pts.reshape((-1, 1, 2))

triangle_color = (0, 0, 255) # BGR color for Red
is_closed = True # We want to connect the last point to the first
thickness = 3

# Draw the triangle on the white image
cv2.polylines(white_image, [pts], is_closed, triangle_color, thickness)


# --- Display the final image ---
# Create a window to show the image
cv2.imshow('White Image with Shapes', white_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Clean up and close all windows
cv2.destroyAllWindows()
