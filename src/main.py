from metadata.loader import load_domains, load_pipelines
from ingestion.bronze_ingestor import ingest_bronze
from observability.audit_logger import log_event

MOCK_DATA = {
    "customers": [{"customer_id": 1, "email": "a@test.com"}],
    "transactions": [{"transaction_id": "t1", "amount": 100}],
    "shipments": [{"shipment_id": "s1", "status": "DELIVERED"}],
}

def run():
    for domain_obj in load_domains():
        domain = domain_obj["name"]
        pipelines = load_pipelines(domain)

        for pipeline in pipelines:
            dataset = pipeline["name"]
            try:
                rows = ingest_bronze(domain, dataset, MOCK_DATA.get(dataset, []))
                log_event(domain, dataset, rows, "SUCCESS")
            except Exception as e:
                log_event(domain, dataset, 0, "FAILED", str(e))

if __name__ == "__main__":
    run()
