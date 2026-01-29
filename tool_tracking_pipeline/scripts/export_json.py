import json
import os

def export(frames, out_path="output/tool_motion.json"):
    os.makedirs("output", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({"frames": frames}, f, indent=2)
    print("[OK] Exported tool_motion.json")
