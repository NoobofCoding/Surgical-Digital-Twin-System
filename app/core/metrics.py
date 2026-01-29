import numpy as np

def path_deviation(trainee, expert):
    return float(np.mean(np.linalg.norm(trainee - expert, axis=1)))

def motion_smoothness(traj):
    diffs = np.diff(traj, axis=0)
    return float(np.mean(np.linalg.norm(diffs, axis=1)))
