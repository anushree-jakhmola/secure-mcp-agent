"""
PII Detection and Redaction

Detects and redacts Personally Identifiable Information (PII)
from already-normalized input.

Supported PII:
- Email Address
- Phone Number
- PAN Number
- Aadhaar Number
"""

import re

from guardrails.audit_logger import log_event

# ----------------------------------------------------
# Regex Patterns
# ----------------------------------------------------

PII_PATTERNS = {
    "EMAIL": (
        re.compile(
            r"\b[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}\b",
            re.IGNORECASE,
        ),
        "[EMAIL_REDACTED]",
    ),

    "AADHAAR": (
        re.compile(
            r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b"
        ),
        "[AADHAAR_REDACTED]",
    ),

    "PHONE": (
        re.compile(
            r"(?:\+91[\s\-]?)?(?:\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}|\d{10})"
        ),
        "[PHONE_REDACTED]",
    ),

    "PAN": (
        re.compile(
            r"\b[a-zA-Z]{5}[- ]?\d{4}[- ]?[a-zA-Z]\b",
            re.IGNORECASE,
        ),
        "[PAN_REDACTED]",
    ),
}


# ----------------------------------------------------
# Detection
# ----------------------------------------------------

def detect_pii(text: str) -> dict:
    """
    Detect supported PII entities.

    Returns:
        {
            "EMAIL": [...],
            "PHONE": [...],
            "PAN": [...],
            "AADHAAR": [...]
        }
    """

    detected = {}

    for name, (pattern, _) in PII_PATTERNS.items():

        matches = pattern.findall(text)

        if matches:
            detected[name] = matches

    return detected


# ----------------------------------------------------
# Redaction
# ----------------------------------------------------

def redact_pii(text: str) -> str:
    """
    Detect and redact supported PII.

    Logs only the number of detected entities,
    never the actual sensitive values.
    """

    sanitized = text

    detected = detect_pii(text)

    for _, (pattern, replacement) in PII_PATTERNS.items():

        sanitized = pattern.sub(
            replacement,
            sanitized,
        )

    if detected:

        summary = " ".join(
            f"{name}:{len(values)}"
            for name, values in detected.items()
        )

        log_event(
            event_type="PII_REDACTED",
            details=summary,
            guardrail="PII_GUARDRAIL",
            severity="INFO",
        )

    return sanitized