import cv2
from utils.video_io import open_video
from utils.visualization import show_frame

def main():
    cap = open_video(0)  # webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        show_frame("Color Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    # print("Color Object Tracker Pipeline")

if __name__ == "__main__":
    main()
