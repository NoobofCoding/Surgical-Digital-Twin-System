import json
import os

def export_trajectory_json(trajectory_3d, velocities, output_path="output/trajectory.json"):
    """
    Export 3D trajectory and velocities to JSON
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    trajectory_data = []

    for i, (frame, vel_frame) in enumerate(zip(trajectory_3d, velocities)):
        for p, v in zip(frame, vel_frame):
            trajectory_data.append({
                "t": i * 0.05,  # timestamp in seconds
                "pos": p,
                "vel": v
            })

    with open(output_path, "w") as f:
        json.dump({"trajectory": trajectory_data}, f, indent=2)

    print(f"Trajectory JSON saved to {output_path}")
