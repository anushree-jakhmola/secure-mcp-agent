"""
File Guardrail Security Tests

Validates secure file access against
path traversal and unauthorized access attacks.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.file_tool import read_allowed_file


def expect_success(name, filename):

    try:
        read_allowed_file(filename)
        print(f"✅ PASS | {name}")
        return True

    except Exception as error:

        print(f"❌ FAIL | {name}")
        print(f"Input    : {filename}")
        print(f"Error    : {error}")
        print()

        return False


def expect_failure(name, filename, expected_exception):

    try:

        read_allowed_file(filename)

        print(f"❌ FAIL | {name}")
        print("Expected request to be blocked.")
        print()

        return False

    except expected_exception:

        print(f"✅ PASS | {name}")
        return True

    except Exception as error:

        print(f"❌ FAIL | {name}")
        print(f"Wrong exception: {type(error).__name__}")
        print(error)
        print()

        return False


def main():

    passed = 0
    total = 0

    # =====================================================
    # VALID FILE ACCESS
    # =====================================================

    total += 1
    if expect_success(
        "Valid TXT File",
        "ai_safety_policy.txt",
    ):
        passed += 1

    # =====================================================
    # EMPTY INPUT
    # =====================================================

    total += 1
    if expect_failure(
        "Empty Filename",
        "",
        ValueError,
    ):
        passed += 1

    total += 1
    if expect_failure(
        "Whitespace Filename",
        "   ",
        ValueError,
    ):
        passed += 1

    # =====================================================
    # PATH TRAVERSAL (PermissionError Expected)
    # =====================================================

    permission_error_attacks = [

        "../../../secret.txt",

        "..\\..\\secret.txt",

        "../../../../etc/passwd",

        "/etc/passwd",

        "../README.md",

        "../../audit.log",

        "../../../.env",

    ]

    for attack in permission_error_attacks:

        total += 1

        if expect_failure(
            f"Traversal: {attack}",
            attack,
            PermissionError,
        ):
            passed += 1

    # =====================================================
    # INVALID PATHS (FileNotFoundError Expected)
    # =====================================================

    file_not_found_attacks = [

        "~/Documents/file.txt",

        "....//secret.txt",

    ]

    for attack in file_not_found_attacks:

        total += 1

        if expect_failure(
            f"Invalid Path: {attack}",
            attack,
            FileNotFoundError,
        ):
            passed += 1

    # =====================================================
    # UNSUPPORTED EXTENSIONS
    # =====================================================

    blocked_extensions = [

        "virus.exe",

        "database.db",

        "script.py",

        "archive.zip",

    ]

    for attack in blocked_extensions:

        total += 1

        if expect_failure(
            f"Extension: {attack}",
            attack,
            PermissionError,
        ):
            passed += 1

    # =====================================================
    # NON-EXISTENT FILE
    # =====================================================

    total += 1

    if expect_failure(
        "Missing File",
        "does_not_exist.txt",
        FileNotFoundError,
    ):
        passed += 1

    print("\n" + "=" * 60)
    print("FILE GUARDRAIL TEST SUMMARY")
    print("=" * 60)
    print(f"Passed : {passed}")
    print(f"Failed : {total-passed}")
    print(f"Total  : {total}")
    print("=" * 60)

    assert passed == total, "Some file guardrail tests failed."


if __name__ == "__main__":
    main()