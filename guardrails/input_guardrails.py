"""
Input Guardrails

1. Prompt Injection Detection
2. PII Redaction
"""

from guardrails.pii_guardrail import redact_pii
from guardrails.security_policy import BLOCKED_PATTERNS
from guardrails.audit_logger import log_event

def check_prompt_injection(user_input: str) -> tuple[bool, str]:
    """
    Detect blocked patterns.
    """

    normalized_input = user_input.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in normalized_input:
            log_event(
                "PROMPT_INJECTION_BLOCKED",
                user_input,
            )
            return (
                False,
                f"Blocked by security policy: '{pattern}' detected."
            )

    return True, "Input passed validation."


def secure_input_pipeline(
    user_input: str,
) -> tuple[bool, str]:
    """
    Multi-layer input security.

    Returns:
        (allowed, processed_input)
    """

    allowed, message = check_prompt_injection(
        user_input
    )

    if not allowed:
        return False, message

    sanitized_input = redact_pii(
        user_input
    )

    return True, sanitized_input