from pathlib import Path

from guardrails.security_policy import (
    ALLOWED_FILE_DIRECTORY,
)


def read_allowed_file(
    filename: str,
):
    """
    Read files only from the
    approved knowledge base directory.
    """

    base_path = Path(
        ALLOWED_FILE_DIRECTORY
    ).resolve()

    target_file = (
        base_path / filename
    ).resolve()

    if not str(
        target_file
    ).startswith(
        str(base_path)
    ):
        raise PermissionError(
            "Path traversal detected."
        )

    if not target_file.exists():
        raise FileNotFoundError(
            f"{filename} not found."
        )

    return target_file.read_text(
        encoding="utf-8"
    )