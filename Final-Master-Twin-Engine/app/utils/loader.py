import json

def load_expert(path: str):
    with open(path) as f:
        return json.load(f)
