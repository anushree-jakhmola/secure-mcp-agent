from pathlib import Path

from guardrails.audit_logger import log_event
from guardrails.security_policy import (
    ALLOWED_FILE_DIRECTORY,
)

ALLOWED_EXTENSIONS = {
    ".txt",
    ".md",
}


def read_allowed_file(filename: str):
    """
    Read files only from the approved
    knowledge base directory.
    """

    if not filename or not filename.strip():
        raise ValueError(
            "Filename cannot be empty."
        )
    
    # Normalize Windows path separators
    filename = filename.replace("\\", "/")

    base_path = Path(
        ALLOWED_FILE_DIRECTORY
    ).resolve()

    target_file = (
        base_path / filename
    ).resolve()

    if not str(target_file).startswith(
        str(base_path)
    ):

        log_event(
            event_type="PATH_TRAVERSAL_BLOCKED",
            details=filename,
            guardrail="FILE_GUARDRAIL",
            severity="HIGH",
        )

        raise PermissionError(
            "Path traversal detected."
        )

    if target_file.suffix.lower() not in ALLOWED_EXTENSIONS:

        log_event(
            event_type="FILE_TYPE_BLOCKED",
            details=filename,
            guardrail="FILE_GUARDRAIL",
            severity="HIGH",
        )

        raise PermissionError(
            "Unsupported file type."
        )

    if not target_file.exists():

        raise FileNotFoundError(
            f"{filename} not found."
        )

    log_event(
        event_type="FILE_ACCESS_GRANTED",
        details=filename,
        guardrail="FILE_GUARDRAIL",
        severity="INFO",
    )

    return target_file.read_text(
        encoding="utf-8"
    )