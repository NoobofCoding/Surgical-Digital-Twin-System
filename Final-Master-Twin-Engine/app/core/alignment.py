import numpy as np

def align_trajectories(trainee, expert):
    min_len = min(len(trainee), len(expert))
    return (
        np.array(trainee[:min_len]),
        np.array(expert[:min_len])
    )
