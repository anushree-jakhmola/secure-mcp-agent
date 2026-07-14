"""
Tool Guardrail Security Tests

Validates MCP tool authorization.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from guardrails.tool_guardrails import authorize_tool


def expect_allowed(name, tool_name):

    try:

        allowed, _ = authorize_tool(tool_name)

        if allowed:
            print(f"✅ PASS | {name}")
            return True

        print(f"❌ FAIL | {name}")
        print(f"Expected tool '{tool_name}' to be allowed.\n")
        return False

    except Exception as error:

        print(f"❌ FAIL | {name}")
        print(error)
        print()

        return False


def expect_denied(name, tool_name):

    try:

        allowed, _ = authorize_tool(tool_name)

        if not allowed:
            print(f"✅ PASS | {name}")
            return True

        print(f"❌ FAIL | {name}")
        print(f"Expected tool '{tool_name}' to be denied.\n")
        return False

    except Exception as error:

        print(f"❌ FAIL | {name}")
        print(error)
        print()

        return False


def expect_exception(name, tool_name, exception_type):

    try:

        authorize_tool(tool_name)

        print(f"❌ FAIL | {name}")
        print("Expected an exception.\n")
        return False

    except exception_type:

        print(f"✅ PASS | {name}")
        return True

    except Exception as error:

        print(f"❌ FAIL | {name}")
        print(type(error).__name__)
        print(error)
        print()

        return False


def main():

    passed = 0
    total = 0

    # ===================================================
    # VALID TOOLS
    # ===================================================

    valid_tools = [

        "knowledge_base",

        "policy_lookup",

        "file_access",

        "system_info",

        "Knowledge_Base",

        "POLICY_LOOKUP",

        "policy-lookup",

        "policy lookup",

        "System Info",

    ]

    for tool in valid_tools:

        total += 1

        if expect_allowed(
            f"Allowed: {tool}",
            tool,
        ):
            passed += 1

    # ===================================================
    # INVALID TOOLS
    # ===================================================

    invalid_tools = [

        "delete_database",

        "shell",

        "terminal",

        "root",

        "admin",

        "execute_code",

        "internet",

        "browser",

    ]

    for tool in invalid_tools:

        total += 1

        if expect_denied(
            f"Denied: {tool}",
            tool,
        ):
            passed += 1

    # ===================================================
    # INVALID INPUT
    # ===================================================

    invalid_inputs = [

        "",

        "     ",

        None,

        123,

        [],

        {},

    ]

    for value in invalid_inputs:

        total += 1

        if expect_exception(
            f"Invalid Input: {value}",
            value,
            ValueError,
        ):
            passed += 1

    print("\n" + "=" * 60)
    print("TOOL GUARDRAIL TEST SUMMARY")
    print("=" * 60)
    print(f"Passed : {passed}")
    print(f"Failed : {total-passed}")
    print(f"Total  : {total}")
    print("=" * 60)

    assert passed == total, "Some tool guardrail tests failed."


if __name__ == "__main__":
    main()