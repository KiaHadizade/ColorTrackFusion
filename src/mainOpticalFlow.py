import cv2
from utils.video_io import open_video
from utils.visualization import draw_bbox
from detection.hsv_detector import detect_hsv_object
from detection.color_ranges import COLOR_RANGES
from tracking.camshift_tracker import CamShiftTracker
from tracking.optical_flow_tracker import OpticalFlowTracker
from tracking.fusion import fuse_bbox

def main():
    cap = open_video(0)

    camshift_tracker = CamShiftTracker()
    flow_tracker = OpticalFlowTracker()
    initialized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not initialized:
            print("1")
            for _, color_range in COLOR_RANGES.items():
                bbox = detect_hsv_object(frame, color_range)

                if bbox:
                    print("22")
                    camshift_tracker.initialize(frame, bbox)
                    flow_tracker.initialize(frame, bbox)
                    initialized = True
        else:
            print("333")
            cam_bbox = camshift_tracker.track(frame)
            flow_pts = flow_tracker.track(frame)

            if cam_bbox is None:
                print("4444")
                initialized = False # Re-detect
                continue
            
            print("55555")
            fused_bbox = fuse_bbox(cam_bbox, flow_pts)
            draw_bbox(frame, fused_bbox, (0, 255, 0))

        cv2.imshow("OpticalFlow Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()