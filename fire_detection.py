import cv2
import numpy as np

# def detect_fire(frame):
#     # Convert the frame to grayscale
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply GaussianBlur to reduce noise and improve detection
#     blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

#     # Use the Absolute Difference to identify changes in the scene
#     frame_delta = cv2.absdiff(blurred_frame, cv2.convertScaleAbs(blurred_frame))

#     # Apply threshold to create a binary image
#     _, thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)

#     # Dilate the thresholded image to fill in holes
#     dilated = cv2.dilate(thresh, None, iterations=2)

#     # Find contours in the dilated image
#     contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Check for contours indicating fire
#     for contour in contours:
#         if cv2.contourArea(contour) > 1000:  # Adjust the area threshold as needed
#             return True

#     return False


# # # # # # # TEST 2# # # # # # # # # # 
# FOR TESTING WITH ANY FRAME
def detect_fire(frame):
    return np.any(frame)


# # # # # # # TEST 3 # # # # # # # # # # 
# def detect_fire(frame):
#     # Convert the frame to HSV color space
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define the color range for fire-like color (red-orange)
#     lower_color = np.array([0, 100, 100])
#     upper_color = np.array([20, 255, 255])

#     # Create a mask for the specified color range
#     mask = cv2.inRange(hsv_frame, lower_color, upper_color)

#     # Count the non-zero pixels in the mask
#     non_zero_count = cv2.countNonZero(mask)

#     # Set a threshold for the number of non-zero pixels to consider fire
#     fire_threshold = 500000

#     # Return True if fire is detected based on the threshold
#     return non_zero_count > fire_threshold
