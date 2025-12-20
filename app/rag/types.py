from typing import List, Dict
from dataclasses import dataclass


@dataclass
class RAGResponse:
    answer: str
    sources: List[Dict]
    security_flags: Dict
    request_id: str
