"""
Input Guardrails

Responsible for detecting prompt injection
and unsafe instructions before they reach
the agent.
"""

from guardrails.security_policy import BLOCKED_PATTERNS


def check_prompt_injection(user_input: str) -> tuple[bool, str]:
    """
    Returns:
        (True, message)  -> safe
        (False, reason)  -> blocked
    """

    normalized_input = user_input.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in normalized_input:
            return (
                False,
                f"Blocked by security policy: '{pattern}' detected."
            )

    return True, "Input passed validation."