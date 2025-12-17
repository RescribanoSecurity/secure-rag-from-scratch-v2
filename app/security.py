from __future__ import annotations

import re
from typing import Tuple


# Common prompt injection patterns
SUSPICIOUS_PATTERNS = [
    r"ignore (all|previous) instructions",
    r"disregard the above",
    r"act as .*",
    r"reveal .*prompt",
    r"show .*system prompt",
    r"you are now .*",
    r"bypass .*security",
    r"print .*password",
    r"print .*token",
]


def normalize_query(query: str) -> str:
    """Normalizes the query to avoid basic tricks."""
    return query.strip().lower()


def detect_prompt_injection(query: str) -> Tuple[bool, str]:
    """
    Detects basic prompt injection attempts.
    Returns (is_malicious, reason)
    """
    normalized = normalize_query(query)

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, normalized):
            return True, f"Matched suspicious pattern: {pattern}"

    return False, "OK"
