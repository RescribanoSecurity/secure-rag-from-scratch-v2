# security/models.py
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class SecurityAction(str, Enum):
    ALLOW = "allow"
    WARN = "warn"        # útil si quieres mostrar bandera en UI sin bloquear
    REDACT = "redact"
    BLOCK = "block"


@dataclass(frozen=True)
class SecurityFinding:
    category: str                 # e.g. "PII_EMAIL", "SECRET_API_KEY"
    severity: int                 # 1..5
    confidence: float             # 0..1
    message: str                  # explicación corta
    evidence: Optional[str] = None  # fragmento mínimo (mejor truncado)


@dataclass
class SecurityResult:
    action: SecurityAction
    risk_score: int               # 0..100
    findings: List[SecurityFinding] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)
