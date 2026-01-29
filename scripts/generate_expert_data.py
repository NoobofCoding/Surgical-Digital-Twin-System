import json
import numpy as np
import os

os.makedirs("app/data/expert", exist_ok=True)

trajectory = []
timestamps = []
collisions = []

for i in range(120):
    x = i * 0.01
    y = np.sin(i * 0.04) * 0.015
    z = i * 0.004

    trajectory.append([x, y, z])
    timestamps.append(i * 0.05)
    collisions.append(False)

expert = {
    "task": "suturing",
    "trajectory": trajectory,
    "timestamps": timestamps,
    "collisions": collisions
}

with open("app/data/expert/suturing.json", "w") as f:
    json.dump(expert, f, indent=2)

print("✔ Expert motion data generated")
