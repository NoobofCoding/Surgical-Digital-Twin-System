import cv2
import os

def capture_video_frames(video_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("OpenCV failed to open the video file")

    frames = []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in video: {total}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        raise RuntimeError("Video loaded but no frames were read")

    print(f"Captured {len(frames)} frames from video")
    return frames
