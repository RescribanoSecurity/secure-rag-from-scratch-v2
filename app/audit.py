import json
import hashlib
from datetime import datetime


def audit_event(event_type: str, query: str, details: dict):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "query_hash": hashlib.sha256(query.encode()).hexdigest(),
        "details": details,
    }

    # stdout logging (cloud-ready)
    print(json.dumps(event))

