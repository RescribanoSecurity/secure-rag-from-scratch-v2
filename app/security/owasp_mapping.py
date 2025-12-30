from typing import Dict, List

# Map from your internal "reasons" to OWASP LLM Top 10 entries
REASON_TO_OWASP: Dict[str, List[Dict]] = {
    "prompt_injection": [
        {
            "owasp_id": "LLM01",
            "owasp_name": "Prompt Injection",
            "risk_level": "High",
            "description": "User attempted to override system instructions.",
        }
    ],
    "instruction_override": [
        {
            "owasp_id": "LLM01",
            "owasp_name": "Prompt Injection",
            "risk_level": "High",
            "description": "User attempted role / instruction takeover.",
        }
    ],
    "security_bypass": [
        {
            "owasp_id": "LLM02",
            "owasp_name": "Insecure Output Handling",
            "risk_level": "High",
            "description": "Attempt to disable or bypass security controls.",
        }
    ],
    "data_exfiltration": [
        {
            "owasp_id": "LLM06",
            "owasp_name": "Sensitive Data Exposure",
            "risk_level": "High",
            "description": "Attempt to extract sensitive or bulk data.",
        }
    ],
}

# Simple catalog of controls you apply
CONTROL_CATALOG: Dict[str, Dict] = {
    "IS-01": {"name": "Input validation & pattern detection"},
    "IS-02": {"name": "Instruction isolation"},
    "PE-01": {"name": "Policy enforcement (block)"},
    "LOG-01": {"name": "Security audit logging"},
}

# Which controls are applied per OWASP entry
OWASP_TO_CONTROLS: Dict[str, List[str]] = {
    "LLM01": ["IS-01", "IS-02"],
    "LLM02": ["PE-01"],
    "LLM06": ["IS-01", "LOG-01"],
}
