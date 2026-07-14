"""
Output Guardrails

Protect responses before they leave
the Secure MCP Agent.
"""

import re

from guardrails.audit_logger import log_event
from guardrails.pii_guardrail import redact_pii

# ----------------------------------------------------
# Patterns
# ----------------------------------------------------

PROMPT_LEAKAGE_PATTERNS = [
    "system prompt",
    "developer instructions",
    "hidden prompt",
    "internal instructions",
]

FILE_PATH_PATTERN = re.compile(
    r"(/Users/[^\s]+|C:\\Users\\[^\s]+|knowledge_base/[^\s]+)",
    re.IGNORECASE,
)


def remove_prompt_leakage(text: str) -> str:
    """
    Remove sensitive prompt-related phrases.
    """

    sanitized = text

    for phrase in PROMPT_LEAKAGE_PATTERNS:

        if re.search(
            re.escape(phrase),
            sanitized,
            flags=re.IGNORECASE,
        ):

            log_event(
                event_type="PROMPT_LEAKAGE_REMOVED",
                details=phrase,
                guardrail="OUTPUT_GUARDRAIL",
                severity="HIGH",
            )

            sanitized = re.sub(
                re.escape(phrase),
                "[REDACTED]",
                sanitized,
                flags=re.IGNORECASE,
            )

    return sanitized


def remove_file_paths(text: str) -> str:
    """
    Remove internal file paths.
    """

    if FILE_PATH_PATTERN.search(text):

        log_event(
            event_type="FILE_PATH_REDACTED",
            details="Internal path removed",
            guardrail="OUTPUT_GUARDRAIL",
            severity="INFO",
        )

    return FILE_PATH_PATTERN.sub(
        "[PATH_REDACTED]",
        text,
    )


def secure_output_pipeline(
    output_text: str,
) -> str:
    """
    Apply layered output security.
    """

    sanitized = redact_pii(
        output_text
    )

    sanitized = remove_prompt_leakage(
        sanitized
    )

    sanitized = remove_file_paths(
        sanitized
    )

    return sanitized