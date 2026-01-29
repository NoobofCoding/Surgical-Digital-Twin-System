import numpy as np

def smooth_trajectory(trajectory, alpha=0.6):
    if len(trajectory) == 0:
        raise ValueError("Empty trajectory — cannot smooth")

    smoothed = []
    prev_frame = trajectory[0]
    smoothed.append(prev_frame)

    for frame in trajectory[1:]:
        smoothed_frame = []
        for p, prev_p in zip(frame, prev_frame):
            smoothed_frame.append([
                alpha * p[0] + (1-alpha) * prev_p[0],
                alpha * p[1] + (1-alpha) * prev_p[1],
                alpha * p[2] + (1-alpha) * prev_p[2]
            ])
        smoothed.append(smoothed_frame)
        prev_frame = smoothed_frame

    return smoothed


def compute_velocity(smoothed_trajectory, delta_t=0.05):
    """
    Compute velocity magnitude for each keypoint per frame
    """
    velocities = []
    prev_frame = smoothed_trajectory[0]
    velocities.append([0.0]*len(prev_frame))

    for frame in smoothed_trajectory[1:]:
        frame_vel = []
        for p, prev_p in zip(frame, prev_frame):
            v = np.linalg.norm(np.array(p) - np.array(prev_p)) / delta_t
            frame_vel.append(v)
        velocities.append(frame_vel)
        prev_frame = frame

    return velocities
