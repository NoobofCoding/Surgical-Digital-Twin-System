from scripts.capture_video import capture_video_frames
from scripts.detect_2d_keypoints import detect_2d_keypoints
from scripts.reconstruct_3d import reconstruct_3d
from scripts.filter_smooth import smooth_trajectory, compute_velocity
from scripts.export_json import export_trajectory_json

def main():
    video_path = "videos/sample_surgery.mp4"

    print("Step 1: Capturing video frames...")
    frames = capture_video_frames(video_path)

    print("Step 2: Detecting 2D keypoints...")
    keypoints_2d = detect_2d_keypoints(frames)

    print("Step 3: Reconstructing 3D trajectory...")
    trajectory_3d = reconstruct_3d(keypoints_2d)

    print("Step 4: Smoothing trajectory...")
    smoothed = smooth_trajectory(trajectory_3d)
    velocities = compute_velocity(smoothed)

    print("Step 5: Exporting JSON...")
    export_trajectory_json(smoothed, velocities)

if __name__ == "__main__":
    main()
