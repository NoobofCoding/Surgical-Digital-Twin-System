import cv2
import numpy as np

def extract_tool_axis(edges):
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=60,
        minLineLength=40,
        maxLineGap=15
    )

    if lines is None:
        return None

    # Collect all significant lines
    valid_lines = []
    for l in lines:
        x1,y1,x2,y2 = l[0]
        length = np.linalg.norm([x2-x1, y2-y1])
        if length > 40:
            valid_lines.append((x1,y1,x2,y2,length))

    if len(valid_lines) == 0:
        return None

    # Compute average direction
    dx = np.mean([x2-x1 for x1,y1,x2,y2,_ in valid_lines])
    dy = np.mean([y2-y1 for x1,y1,x2,y2,_ in valid_lines])

    # Compute average center
    cx = np.mean([(x1+x2)/2 for x1,y1,x2,y2,_ in valid_lines])
    cy = np.mean([(y1+y2)/2 for x1,y1,x2,y2,_ in valid_lines])

    p1 = (int(cx - dx), int(cy - dy))
    p2 = (int(cx + dx), int(cy + dy))

    return p1, p2
