from typing import Dict, List
import re


class InputSecurityAnalyzer:
    """
    Analyzes user input queries to detect potentially malicious
    or unsafe patterns such as prompt injection or instruction override.
    """

    def __init__(self):
        self.patterns = {
            "prompt_injection": [
                r"ignore .*instructions",
                r"disregard .*instructions",
                r"system prompt",
                r"developer message",
            ],
            "instruction_override": [
                r"you are now",
                r"act as",
                r"forget (all|previous)",
            ],
            "data_exfiltration": [
                r"show me all",
                r"dump .* data",
                r"export .* database",
            ],
            "security_bypass": [
                r"disable security.*",
                r"bypass .*restrictions",
                r"no .*limitations",
            ],
        }

        # Risk weight per category
        self.risk_weights = {
            "prompt_injection": 40,
            "instruction_override": 30,
            "data_exfiltration": 50,
            "security_bypass": 50,
        }

        # 🔒 Categories that are ALWAYS blocked (policy decision)
        self.hard_block_categories = {
            "prompt_injection",
        }

    def analyze(self, query: str) -> Dict:
        query_lower = query.lower()
        reasons: List[str] = []
        risk_score = 0

        for category, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    reasons.append(category)
                    risk_score += self.risk_weights.get(category, 0)
                    break

        action = self._decide_action(reasons, risk_score)

        return {
            "allowed": action != "block",
            "action": action,
            "risk_score": risk_score,
            "reasons": reasons,
        }

    def _decide_action(self, reasons: List[str], risk_score: int) -> str:
        # 🔒 Hard block rules (explicit policy)
        for reason in reasons:
            if reason in self.hard_block_categories:
                return "block"

        # Score-based enforcement
        if risk_score >= 70:
            return "block"
        if risk_score >= 30:
            return "warn"
        return "allow"
