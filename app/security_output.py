import re
from typing import List


EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"\+?\d[\d\s\-]{7,}\d"


def detect_pii(text: str) -> List[str]:
    findings = []

    if re.search(EMAIL_REGEX, text):
        findings.append("email")

    if re.search(PHONE_REGEX, text):
        findings.append("phone")

    return findings


def redact_pii(text: str) -> str:
    text = re.sub(EMAIL_REGEX, "[REDACTED_EMAIL]", text)
    text = re.sub(PHONE_REGEX, "[REDACTED_PHONE]", text)
    return text

