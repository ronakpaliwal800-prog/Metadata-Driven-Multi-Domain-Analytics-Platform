from datetime import datetime

def log_event(domain, dataset, rows, status, error=None):
    log = {
        "domain": domain,
        "dataset": dataset,
        "rows": rows,
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
        "error": error
    }
    print("AUDIT_LOG:", log)
