"""
Input Normalization Layer

This module standardizes user input before
security checks are performed.

Normalization is ONLY used for detection.
The original user input should be preserved
for final output whenever possible.
"""

import re
import unicodedata


EMAIL_REPLACEMENTS = {
    r"\(at\)": "@",
    r"\[at\]": "@",
    r"\bat\b": "@",
    r"\(dot\)": ".",
    r"\[dot\]": ".",
    r"\bdot\b": ".",
}


def normalize_input(text: str) -> str:
    """
    Normalize user input for security detection.

    This function does NOT attempt to preserve
    formatting. It produces a canonical form
    used only by the guardrails.
    """

    # ----------------------------------
    # Unicode normalization
    # ----------------------------------

    text = unicodedata.normalize("NFKC", text)

    # ----------------------------------
    # Remove zero-width characters
    # ----------------------------------

    text = re.sub(
        r"[\u200B-\u200D\uFEFF]",
        "",
        text,
    )

    # ----------------------------------
    # Lowercase for matching
    # ----------------------------------

    text = text.lower()

    # ----------------------------------
    # Normalize whitespace
    # ----------------------------------

    text = re.sub(r"\s+", " ", text)

    # ----------------------------------
    # Normalize common email obfuscations
    # ----------------------------------

    for pattern, replacement in EMAIL_REPLACEMENTS.items():
        text = re.sub(
            pattern,
            replacement,
            text,
            flags=re.IGNORECASE,
        )

    # ----------------------------------
    # Remove spaces around @
    # john @ gmail.com
    # ->
    # john@gmail.com
    # ----------------------------------

    text = re.sub(
        r"\s*@\s*",
        "@",
        text,
    )

    # ----------------------------------
    # Remove spaces around .
    # john . doe
    # ->
    # john.doe
    # ----------------------------------

    text = re.sub(
        r"\s*\.\s*",
        ".",
        text,
    )

    # ----------------------------------
    # Normalize phone separators
    # ----------------------------------

    text = re.sub(
        r"(?<=\d)[\s\-\(\)\.]+(?=\d)",
        "",
        text,
    )

    # ----------------------------------
    # Collapse repeated punctuation
    # ----------------------------------

    text = re.sub(
        r"\.{2,}",
        ".",
        text,
    )

    return text.strip()