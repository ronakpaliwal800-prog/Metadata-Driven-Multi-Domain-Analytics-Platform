import yaml
from pathlib import Path

METADATA_DIR = Path("metadata")

def load_domains():
    with open(METADATA_DIR / "domains.yaml") as f:
        return yaml.safe_load(f)["domains"]

def load_pipelines(domain):
    with open(METADATA_DIR / "pipelines" / f"{domain}.yaml") as f:
        return yaml.safe_load(f)["pipelines"]
