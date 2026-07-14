"""
Audit Logger

Records security-relevant events generated
by the Secure MCP Agent.
"""

from datetime import datetime


def log_event(
    event_type: str,
    details: str,
    guardrail: str = "UNKNOWN",
    severity: str = "INFO",
) -> None:
    """
    Append a structured security event to audit.log.
    """

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = (
        f"[{timestamp}] "
        f"[{severity}] "
        f"[{guardrail}] "
        f"{event_type}: "
        f"{details}\n"
    )

    with open(
        "audit.log",
        "a",
        encoding="utf-8",
    ) as log_file:
        log_file.write(log_entry)