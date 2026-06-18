"""
Audit Logger

Tracks security-relevant events.
"""

from datetime import datetime


def log_event(
    event_type: str,
    details: str,
) -> None:
    """
    Append security events to audit.log
    """

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = (
        f"[{timestamp}] "
        f"{event_type}: "
        f"{details}\n"
    )

    with open(
        "audit.log",
        "a",
        encoding="utf-8",
    ) as log_file:
        log_file.write(log_entry)