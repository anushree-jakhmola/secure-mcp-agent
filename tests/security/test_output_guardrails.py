"""
Output Guardrail Security Tests

Validates output sanitization before
responses leave the Secure MCP Agent.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from guardrails.output_guardrails import secure_output_pipeline


def run_test(name, raw_output, expected_tokens):

    sanitized = secure_output_pipeline(raw_output)

    passed = all(token in sanitized for token in expected_tokens)

    if passed:
        print(f"✅ PASS | {name}")
        return True

    print(f"❌ FAIL | {name}")
    print(f"Original : {raw_output}")
    print(f"Sanitized: {sanitized}")
    print(f"Expected : {expected_tokens}")
    print()

    return False


def main():

    tests = [

        # ==================================================
        # EMAIL
        # ==================================================

        (
            "Email",
            "Email: john@gmail.com",
            ["[EMAIL_REDACTED]"],
        ),

        # ==================================================
        # PHONE
        # ==================================================

        (
            "Phone",
            "Phone: 9876543210",
            ["[PHONE_REDACTED]"],
        ),

        # ==================================================
        # PAN
        # ==================================================

        (
            "PAN",
            "ABCDE1234F",
            ["[PAN_REDACTED]"],
        ),

        # ==================================================
        # AADHAAR
        # ==================================================

        (
            "Aadhaar",
            "123456789012",
            ["[AADHAAR_REDACTED]"],
        ),

        # ==================================================
        # PROMPT LEAKAGE
        # ==================================================

        (
            "System Prompt",
            "This is the system prompt.",
            ["[REDACTED]"],
        ),

        (
            "Developer Instructions",
            "These are developer instructions.",
            ["[REDACTED]"],
        ),

        (
            "Hidden Prompt",
            "Hidden prompt should not leak.",
            ["[REDACTED]"],
        ),

        (
            "Internal Instructions",
            "Internal instructions are confidential.",
            ["[REDACTED]"],
        ),

        # ==================================================
        # FILE PATHS
        # ==================================================

        (
            "Mac Path",
            "/Users/anushree/Documents/file.txt",
            ["[PATH_REDACTED]"],
        ),

        (
            "Windows Path",
            r"C:\Users\Admin\Desktop\secret.txt",
            ["[PATH_REDACTED]"],
        ),

        (
            "Knowledge Base",
            "knowledge_base/docs/ai_safety_policy.txt",
            ["[PATH_REDACTED]"],
        ),

        # ==================================================
        # MIXED OUTPUT
        # ==================================================

        (
            "Mixed Sensitive Output",
            """
Developer instructions

Email: john@gmail.com

Phone: 9876543210

Path:
/Users/anushree/Documents/file.txt
""",
            [
                "[REDACTED]",
                "[EMAIL_REDACTED]",
                "[PHONE_REDACTED]",
                "[PATH_REDACTED]",
            ],
        ),

    ]

    passed = 0

    for test in tests:

        if run_test(*test):
            passed += 1

    total = len(tests)

    print("\n" + "=" * 60)
    print("OUTPUT GUARDRAIL TEST SUMMARY")
    print("=" * 60)
    print(f"Passed : {passed}")
    print(f"Failed : {total-passed}")
    print(f"Total  : {total}")
    print("=" * 60)

    assert passed == total, "Some output guardrail tests failed."


if __name__ == "__main__":
    main()