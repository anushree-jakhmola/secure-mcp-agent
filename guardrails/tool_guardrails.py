"""
Tool Authorization Guardrails
"""

from guardrails.security_policy import ALLOWED_TOOLS


def authorize_tool(tool_name: str) -> tuple[bool, str]:
    """
    Check whether a tool is allowed.
    """

    if tool_name not in ALLOWED_TOOLS:
        return (
            False,
            f"Tool '{tool_name}' is not authorized."
        )

    return (
        True,
        f"Tool '{tool_name}' authorized."
    )