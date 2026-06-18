"""
Output Guardrails

Protect responses before they leave
the system.
"""

from guardrails.pii_guardrail import redact_pii


def secure_output_pipeline(
    output_text: str,
) -> str:
    """
    Apply output security controls.
    """

    sanitized_output = redact_pii(
        output_text
    )

    return sanitized_output