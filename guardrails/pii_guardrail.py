"""
PII Detection and Redaction
"""

import re


EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

PHONE_PATTERN = r"\b\d{10}\b"

PAN_PATTERN = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"

AADHAAR_PATTERN = r"\b\d{4}\s?\d{4}\s?\d{4}\b"


def redact_pii(text: str) -> str:
    """
    Redact common PII patterns.
    """

    text = re.sub(
        EMAIL_PATTERN,
        "[EMAIL_REDACTED]",
        text,
    )

    text = re.sub(
        PHONE_PATTERN,
        "[PHONE_REDACTED]",
        text,
    )

    text = re.sub(
        PAN_PATTERN,
        "[PAN_REDACTED]",
        text,
    )

    text = re.sub(
        AADHAAR_PATTERN,
        "[AADHAAR_REDACTED]",
        text,
    )

    return text