import json
from datetime import datetime
from pathlib import Path

def ingest_bronze(domain, dataset, records):
    ingestion_date = datetime.utcnow().date().isoformat()

    base_path = Path("data/bronze") / domain / dataset / f"ingestion_date={ingestion_date}"
    base_path.mkdir(parents=True, exist_ok=True)

    file_path = base_path / "data.json"

    with open(file_path, "w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

    return len(records)
