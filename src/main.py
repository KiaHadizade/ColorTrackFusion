import cv2
from utils.video_io import open_video
from utils.visualization import show_frame, draw_bbox
from detection.hsv_detector import detect_hsv_object
from detection.color_ranges import COLOR_RANGES

def main():
    cap = open_video(0)  # webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # show_frame("Color Object Tracker", frame)
        for _, color_range in COLOR_RANGES.items():
            bbox = detect_hsv_object(frame, color_range)
            if bbox is not None:
                draw_bbox(frame, bbox)

        cv2.imshow("HSV Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
