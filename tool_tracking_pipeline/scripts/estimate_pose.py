import math

def estimate_pose(p1, p2, depth=0.25):
    cx = (p1[0] + p2[0]) / 2
    cy = (p1[1] + p2[1]) / 2

    x = cx / 1000
    y = depth
    z = cy / 1000

    yaw = math.atan2(p2[1]-p1[1], p2[0]-p1[0])

    return [x, y, z], [0, 0, yaw]
