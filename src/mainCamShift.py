import cv2
from utils.video_io import open_video
from utils.visualization import draw_bbox
from detection.hsv_detector import detect_hsv_object
from detection.color_ranges import COLOR_RANGES
from tracking.camshift_tracker import CamShiftTracker

def main():
    cap = open_video(0)

    tracker = CamShiftTracker()
    initialized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not initialized:
            print("1")
            for _, color_range in COLOR_RANGES.items():
                print("22")
                bbox = detect_hsv_object(frame, color_range)
                if bbox is not None:
                    print("333")
                    tracker.initialize(frame, bbox)
                    initialized = True
                    draw_bbox(frame, bbox, (255, 0, 0)) # Blue Init Box
        else:
            print("4444")
            bbox = tracker.track(frame)
            if bbox is None:
                print("55555")
                initialized = False # Re-detect
            else:
                print("666666")
                draw_bbox(frame, bbox) # Green Tracking Box

        cv2.imshow("CamShift Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
