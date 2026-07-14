"""
Normalization Security Tests

Validates the input normalization layer against
common obfuscation techniques.
"""

import sys
from pathlib import Path

# Allow imports from project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from guardrails.input_normalizer import normalize_input


def run_test(name: str, raw_input: str, expected_output: str) -> bool:
    """
    Execute one normalization test.
    """

    actual_output = normalize_input(raw_input)

    if actual_output == expected_output:
        print(f"✅ PASS | {name}")
        return True

    print(f"❌ FAIL | {name}")
    print(f"   Input    : {raw_input}")
    print(f"   Expected : {expected_output}")
    print(f"   Actual   : {actual_output}")
    print()

    return False


def main():

    tests = [

        # -------------------------------------------------
        # Email Normalization
        # -------------------------------------------------

        (
            "Email - Uppercase",
            "JOHN@GMAIL.COM",
            "john@gmail.com",
        ),

        (
            "Email - (at)",
            "john(at)gmail(dot)com",
            "john@gmail.com",
        ),

        (
            "Email - [at]",
            "john[at]gmail[dot]com",
            "john@gmail.com",
        ),

        (
            "Email - Spaces Around @",
            "john @ gmail.com",
            "john@gmail.com",
        ),

        (
            "Email - Spaces Around Dot",
            "john@gmail . com",
            "john@gmail.com",
        ),

        (
            "Email - Mixed Spaces",
            "john . doe @ gmail . com",
            "john.doe@gmail.com",
        ),

        # -------------------------------------------------
        # Whitespace
        # -------------------------------------------------

        (
            "Whitespace - Multiple Spaces",
            "Hello     World",
            "hello world",
        ),

        (
            "Whitespace - Tabs",
            "Hello\t\tWorld",
            "hello world",
        ),

        (
            "Whitespace - Newlines",
            "Hello\n\nWorld",
            "hello world",
        ),

        # -------------------------------------------------
        # Punctuation
        # -------------------------------------------------

        (
            "Repeated Dots",
            "john....doe@gmail.com",
            "john.doe@gmail.com",
        ),

    ]

    passed = 0

    for test in tests:

        if run_test(*test):
            passed += 1

    total = len(tests)

    print("\n" + "=" * 60)
    print("NORMALIZATION TEST SUMMARY")
    print("=" * 60)
    print(f"Passed : {passed}")
    print(f"Failed : {total - passed}")
    print(f"Total  : {total}")
    print("=" * 60)

    assert passed == total, "Some normalization tests failed."


if __name__ == "__main__":
    main()