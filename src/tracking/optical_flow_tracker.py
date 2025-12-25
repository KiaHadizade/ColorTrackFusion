import cv2
import numpy as np

class OpticalFlowTracker:
    def __init__(self):
        self.prev_gray = None
        self.points = None

        self.lk_params = dict(
            winSize=(15, 15),
            maxLevel=2,
            criteria=(
                cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                10,
                0.03
            )
        )

    def initialize(self, frame, bbox):
        x, y, w, h = bbox
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mask = np.zeros_like(gray)
        mask[y:y+h, x:x+w] = 255

        self.points = cv2.goodFeaturesToTrack(
            gray,
            mask=mask,
            maxCorners=100,
            qualityLevel=0.3,
            minDistance=7,
            blockSize=7
        )

        self.prev_gray = gray

    def track(self, frame):
        if self.points is None:
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        next_pts, status, _ = cv2.calcOpticalFlowPyrLK(
            self.prev_gray, gray, self.points, None, **self.lk_params
        )

        good_new = next_pts[status == 1]
        good_old = self.points[status == 1]

        self.prev_gray = gray
        self.points = good_new.reshape(-1, 1, 2)

        return good_new
    