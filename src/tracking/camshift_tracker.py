import cv2
import numpy as np

class CamShiftTracker:
    def __init__(self):
        self.track_window = None
        self.roi_hist = None
        self.term_crit = (
            cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
            10,
            1
        )

    def initialize(self, frame, bbox):
        x, y, w, h = bbox
        self.track_window = (x, y, w, h)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        roi = hsv[y:y+h, x:x+w]

        mask = cv2.inRange(
            roi,
            np.array((94, 80, 2)),
            np.array((126, 255, 255))
        )

        self.roi_hist = cv2.calcHist(
            [roi], [0], mask, [180], [0, 180]
        )

        cv2.normalize(
            self.roi_hist, self.roi_hist, 0, 255, cv2.NORM_MINMAX
        )

    def track(self, frame):
        if self.track_window is None:
            return None

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        back_proj = cv2.calcBackProject(
            [hsv], [0], self.roi_hist, [0, 180], 1
        )

        mask = cv2.inRange(
            hsv,
            np.array((100, 100, 130)),
            np.array((179, 255, 255))
        )

        back_proj = cv2.bitwise_and(back_proj, back_proj, mask=mask)

        ret, self.track_window = cv2.CamShift(
            back_proj, self.track_window, self.term_crit
        )

        pts = cv2.boxPoints(ret)
        pts = pts.astype(int)

        x, y, w, h = cv2.boundingRect(pts)

        roi_prob = back_proj[y:y+h, x:x+w]
        confidence = cv2.mean(roi_prob)[0]

        if confidence < 5:
            self.track_window = None
            return None

        return (x, y, w, h)
