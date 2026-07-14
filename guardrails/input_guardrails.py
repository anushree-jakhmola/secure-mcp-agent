"""
Input Guardrails

Responsibilities:
1. Normalize user input
2. Detect prompt injection
3. Redact PII
"""

from guardrails.audit_logger import log_event
from guardrails.input_normalizer import normalize_input
from guardrails.pii_guardrail import redact_pii
from guardrails.security_policy import BLOCKED_PATTERNS


def check_prompt_injection(normalized_input: str) -> tuple[bool, str]:
    """
    Check normalized input against blocked security patterns.
    """

    for pattern in BLOCKED_PATTERNS:

        if pattern in normalized_input:

            log_event(
                event_type="PROMPT_INJECTION_BLOCKED",
                details=f"Matched pattern: {pattern}",
                guardrail="INPUT_GUARDRAIL",
                severity="HIGH",
            )

            return (
                False,
                f"Blocked by security policy. Matched pattern: '{pattern}'.",
            )

    return True, "Input passed security validation."


def secure_input_pipeline(
    user_input: str,
) -> tuple[bool, str]:
    """
    Complete input security pipeline.
    """

    # Step 1
    normalized_input = normalize_input(
        user_input
    )

    # Step 2
    allowed, message = check_prompt_injection(
        normalized_input
    )

    if not allowed:
        return False, message

    # Step 3
    sanitized_input = redact_pii(
        normalized_input
    )

    return True, sanitized_input