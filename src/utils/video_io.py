import cv2

def open_video(source):
    """
    source: int (webcam) or str (video path)
    """
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise IOError("Cannot open video source")
    return cap
