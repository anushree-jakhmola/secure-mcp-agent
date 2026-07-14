"""
PII Security Tests

Validates detection and redaction of supported
Personally Identifiable Information (PII).
"""

import sys
from pathlib import Path

# Allow imports from project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from guardrails.pii_guardrail import redact_pii


def run_test(name: str, raw_input: str, expected_contains: list[str]) -> bool:
    """
    Execute one PII redaction test.
    """

    output = redact_pii(raw_input)

    passed = all(token in output for token in expected_contains)

    if passed:
        print(f"✅ PASS | {name}")
        return True

    print(f"❌ FAIL | {name}")
    print(f"Input    : {raw_input}")
    print(f"Expected : {expected_contains}")
    print(f"Actual   : {output}")
    print()

    return False


def main():

    tests = [

        # -------------------------------------------------
        # EMAIL
        # -------------------------------------------------

        (
            "Email - Standard",
            "john@gmail.com",
            ["[EMAIL_REDACTED]"],
        ),

        (
            "Email - Uppercase",
            "JOHN@GMAIL.COM",
            ["[EMAIL_REDACTED]"],
        ),

        (
            "Email - Plus Address",
            "john+work@gmail.com",
            ["[EMAIL_REDACTED]"],
        ),

        (
            "Email - Subdomain",
            "john@company.org",
            ["[EMAIL_REDACTED]"],
        ),

        (
            "Email - Dotted Username",
            "john.doe@gmail.com",
            ["[EMAIL_REDACTED]"],
        ),

        # -------------------------------------------------
        # PHONE
        # -------------------------------------------------

        (
            "Phone - Plain",
            "9876543210",
            ["[PHONE_REDACTED]"],
        ),

        (
            "Phone - Hyphen",
            "987-654-3210",
            ["[PHONE_REDACTED]"],
        ),

        (
            "Phone - Spaces",
            "987 654 3210",
            ["[PHONE_REDACTED]"],
        ),

        (
            "Phone - Country Code",
            "+91-9876543210",
            ["[PHONE_REDACTED]"],
        ),

        (
            "Phone - Parentheses",
            "(987)6543210",
            ["[PHONE_REDACTED]"],
        ),

        # -------------------------------------------------
        # PAN
        # -------------------------------------------------

        (
            "PAN - Standard",
            "ABCDE1234F",
            ["[PAN_REDACTED]"],
        ),

        (
            "PAN - Lowercase",
            "abcde1234f",
            ["[PAN_REDACTED]"],
        ),

        (
            "PAN - Hyphen",
            "ABCDE-1234-F",
            ["[PAN_REDACTED]"],
        ),

        (
            "PAN - Spaces",
            "ABCDE 1234 F",
            ["[PAN_REDACTED]"],
        ),

        # -------------------------------------------------
        # Aadhaar
        # -------------------------------------------------

        (
            "Aadhaar - Plain",
            "123456789012",
            ["[AADHAAR_REDACTED]"],
        ),

        (
            "Aadhaar - Spaces",
            "1234 5678 9012",
            ["[AADHAAR_REDACTED]"],
        ),

        (
            "Aadhaar - Hyphen",
            "1234-5678-9012",
            ["[AADHAAR_REDACTED]"],
        ),

        # -------------------------------------------------
        # Mixed PII
        # -------------------------------------------------

        (
            "Mixed PII",
            """
            Email: john@gmail.com
            Phone: 9876543210
            PAN: ABCDE1234F
            Aadhaar: 123456789012
            """,
            [
                "[EMAIL_REDACTED]",
                "[PHONE_REDACTED]",
                "[PAN_REDACTED]",
                "[AADHAAR_REDACTED]",
            ],
        ),
    ]

    passed = 0

    for test in tests:

        if run_test(*test):
            passed += 1

    total = len(tests)

    print("\n" + "=" * 60)
    print("PII TEST SUMMARY")
    print("=" * 60)
    print(f"Passed : {passed}")
    print(f"Failed : {total-passed}")
    print(f"Total  : {total}")
    print("=" * 60)

    assert passed == total, "Some PII tests failed."


if __name__ == "__main__":
    main()