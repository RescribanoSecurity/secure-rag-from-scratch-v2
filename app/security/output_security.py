import re
from typing import Dict, List


class OutputSecurityAnalyzer:
    """
    Output Security v2
    Analyzes LLM output to detect:
    - PII
    - Secrets
    And enforces: allow / redact / block
    """

    def __init__(self):
        self.rules = [
            {
                "category": "PII_EMAIL",
                "pattern": re.compile(
                    r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b",
                    re.IGNORECASE,
                ),
                "severity": 3,
                "action": "redact",
                "redaction": "[REDACTED_EMAIL]",
            },
            {
                "category": "PII_PHONE",
                "pattern": re.compile(r"\b\+?\d[\d\s().-]{7,}\d\b"),
                "severity": 3,
                "action": "redact",
                "redaction": "[REDACTED_PHONE]",
            },
            {
                "category": "SECRET_API_KEY",
                "pattern": re.compile(r"\bsk-[a-zA-Z0-9]{20,}\b"),
                "severity": 5,
                "action": "block",
                "redaction": None,
            },
        ]

    def analyze(self, text: str) -> Dict:
        if not text:
            return self._allow_result()

        findings: List[Dict] = []
        risk_score = 0
        actions = []

        for rule in self.rules:
            matches = rule["pattern"].findall(text)
            if not matches:
                continue

            count = len(matches)
            risk_score += self._calculate_risk(
                severity=rule["severity"],
                occurrences=count,
            )
            actions.append(rule["action"])

            findings.append(
                {
                    "category": rule["category"],
                    "severity": rule["severity"],
                    "count": count,
                }
            )

        # Decision
        if "block" in actions or risk_score >= 80:
            return {
                "action": "block",
                "risk_score": min(risk_score, 100),
                "findings": findings,
                "redacted_text": None,
            }

        if "redact" in actions or risk_score >= 30:
            return {
                "action": "redact",
                "risk_score": min(risk_score, 100),
                "findings": findings,
                "redacted_text": self._redact(text),
            }

        if findings:
            return {
                "action": "warn",
                "risk_score": min(risk_score, 100),
                "findings": findings,
                "redacted_text": text,
            }

        return self._allow_result()

    def _calculate_risk(self, severity: int, occurrences: int) -> int:
        base = {
            1: 5,
            2: 10,
            3: 20,
            4: 40,
            5: 80,
        }.get(severity, 10)

        return base * occurrences

    def _redact(self, text: str) -> str:
        redacted = text
        for rule in self.rules:
            if rule["action"] == "redact":
                redacted = rule["pattern"].sub(rule["redaction"], redacted)
        return redacted

    def _allow_result(self) -> Dict:
        return {
            "action": "allow",
            "risk_score": 0,
            "findings": [],
            "redacted_text": None,
        }
