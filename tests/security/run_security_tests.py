"""
Secure MCP Agent

Master Security Test Runner

Runs every security validation suite and
generates a consolidated security report.
"""

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


TESTS = [

    (
        "Normalization",
        "tests/security/test_normalization.py",
    ),

    (
        "PII",
        "tests/security/test_pii.py",
    ),

    (
        "Prompt Injection",
        "tests/security/test_prompt_injection.py",
    ),

    (
        "File Guardrails",
        "tests/security/test_file_guardrails.py",
    ),

    (
        "Tool Guardrails",
        "tests/security/test_tool_guardrails.py",
    ),

    (
        "Output Guardrails",
        "tests/security/test_output_guardrails.py",
    ),

    (
        "Input Integration",
        "tests/security/test_input_security.py",
    ),

]


def run_test(name, script):

    print(f"\nRunning {name}...")

    result = subprocess.run(
        [sys.executable, script],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    passed = result.returncode == 0

    if passed:

        print("✅ PASS")

    else:

        print("❌ FAIL")

        print(result.stdout)

        print(result.stderr)

    return passed


def main():

    print()

    print("=" * 70)

    print("        SECURE MCP AGENT SECURITY VALIDATION")

    print("=" * 70)

    total = len(TESTS)

    passed = 0

    module_results = []

    for name, script in TESTS:

        success = run_test(
            name,
            script,
        )

        module_results.append(
            (name, success)
        )

        if success:
            passed += 1

    print()

    print("=" * 70)

    print("FINAL SECURITY REPORT")

    print("=" * 70)

    for name, success in module_results:

        status = "PASS ✅" if success else "FAIL ❌"

        print(
            f"{name:<25} {status}"
        )

    print("-" * 70)

    print(f"Modules Passed : {passed}")

    print(f"Modules Failed : {total-passed}")

    score = (
        passed / total
    ) * 100

    print(f"Security Score : {score:.1f}%")

    if passed == total:

        print()

        print("🟢 OVERALL STATUS : SECURE")

    else:

        print()

        print("🔴 OVERALL STATUS : REVIEW REQUIRED")

    print("=" * 70)

    if passed != total:

        sys.exit(1)


if __name__ == "__main__":
    main()