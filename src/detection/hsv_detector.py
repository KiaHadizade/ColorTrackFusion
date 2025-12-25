import cv2
import numpy as np

def detect_hsv_object(frame, color_range, min_area=800):
    """
    Detect object using HSV color thresholding
    Returns bounding box (x, y, width, height) or None
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Handle colors with two HSV ranges (e.g., red)
    if isinstance(color_range["lower"][0], list):
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for low, high in zip(color_range["lower"], color_range["upper"]):
            mask |= cv2.inRange(hsv, np.array(low), np.array(high))
    else:
        mask = cv2.inRange(
            hsv,
            np.array(color_range["lower"]),
            np.array(color_range["upper"])
        )

    # Morphological cleanup
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # Remove small noise
    # mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # Fill gaps inside object

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    largest = max(contours, key=cv2.contourArea)
    if cv2.contourArea(largest) < min_area: # min_area removes false positives
        return None

    return cv2.boundingRect(largest)
