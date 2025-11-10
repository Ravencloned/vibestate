import os
import yaml

def load_secrets(path="secrets.yaml"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return yaml.safe_load(f)
    return {}
