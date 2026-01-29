def reconstruct_3d(keypoints_2d, scale_factor=0.1):
    """
    Approximate 3D reconstruction from 2D keypoints.
    Each landmark gets a z coordinate based on index and scale_factor.
    """
    keypoints_3d = []
    z_base = 0.05  # arbitrary base depth

    for frame in keypoints_2d:
        frame_3d = []
        for i, (x, y) in enumerate(frame):
            z = z_base + i * scale_factor
            frame_3d.append([x, y, z])
        keypoints_3d.append(frame_3d)

    return keypoints_3d
