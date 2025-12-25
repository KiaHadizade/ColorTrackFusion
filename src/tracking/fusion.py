import numpy as np

def fuse_bbox(camshift_bbox, flow_points, margin=10):
    """
    Fuse outputs of two trackers
    """
    if camshift_bbox is None:
        return None

    x, y, w, h = camshift_bbox

    if flow_points is None or len(flow_points) == 0:
        return camshift_bbox

    xs = flow_points[:, 0]
    ys = flow_points[:, 1]

    min_x = min(xs.min(), x)
    min_y = min(ys.min(), y)
    max_x = max(xs.max(), x + w)
    max_y = max(ys.max(), y + h)

    min_x = int(max(min_x - margin, 0))
    min_y = int(max(min_y - margin, 0))
    max_x = int(max_x + margin)
    max_y = int(max_y + margin)

    return (min_x, min_y, max_x - min_x, max_y - min_y)
