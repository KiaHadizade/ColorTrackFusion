import cv2

def draw_bbox(frame, bbox, color=(0, 255, 0), thickness=2):
    x, y, w, h = bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)

def show_frame(window_name, frame):
    cv2.imshow(window_name, frame)