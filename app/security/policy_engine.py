from typing import Dict, List
from app.security.owasp_mapping import REASON_TO_OWASP, OWASP_TO_CONTROLS, CONTROL_CATALOG


def build_policy_violations(security_flags: Dict) -> List[Dict]:
    """
    Translates technical security flags (reasons) into OWASP-mapped policy violations.
    """
    reasons = security_flags.get("reasons", [])
    seen = set()
    violations: List[Dict] = []

    # Expand reasons -> OWASP entries
    for reason in reasons:
        for entry in REASON_TO_OWASP.get(reason, []):
            key = entry["owasp_id"]
            if key in seen:
                continue
            seen.add(key)

            control_ids = OWASP_TO_CONTROLS.get(entry["owasp_id"], [])
            controls_applied = [
                {"control_id": cid, "name": CONTROL_CATALOG[cid]["name"]}
                for cid in control_ids
                if cid in CONTROL_CATALOG
            ]

            violations.append(
                {
                    "owasp_id": entry["owasp_id"],
                    "owasp_name": entry["owasp_name"],
                    "risk_level": entry["risk_level"],
                    "description": entry["description"],
                    "detected_by": [r for r in reasons if r in REASON_TO_OWASP],
                    "controls_applied": controls_applied,
                }
            )

    return violations
