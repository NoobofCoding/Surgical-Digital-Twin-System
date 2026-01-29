import cv2
from scripts.detect_tool_edges import detect_tool_edges
from scripts.extract_tool_axis import extract_tool_axis
from scripts.estimate_pose import estimate_pose
from scripts.export_json import export

cap = cv2.VideoCapture("videos/input.mp4")

frames_out = []
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    edges = detect_tool_edges(frame)
    axis = extract_tool_axis(edges)

    if axis:
        p1, p2 = axis
        pos, rot = estimate_pose(p1, p2)

        frames_out.append({
            "frame": frame_id,
            "pos": pos,
            "rot": rot
        })

    frame_id += 1

cap.release()
export(frames_out)
