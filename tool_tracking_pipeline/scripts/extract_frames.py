import cv2
import os

def extract_frames(video_path, out_dir="frames"):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{out_dir}/{idx:04d}.png", frame)
        idx += 1

    cap.release()
    print(f"[OK] Extracted {idx} frames")
