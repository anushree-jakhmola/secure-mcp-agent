"""
Tool Authorization Guardrails
"""

from guardrails.security_policy import ALLOWED_TOOLS
from guardrails.audit_logger import log_event

def authorize_tool(tool_name: str) -> tuple[bool, str]:
    """
    Check whether a tool is allowed.
    """

    if tool_name not in ALLOWED_TOOLS:

        log_event(
            "TOOL_DENIED",
            tool_name,
        )

        return (
            False,
            f"Tool '{tool_name}' is not authorized."
        )

    log_event(
        "TOOL_AUTHORIZED",
        tool_name,
    )

    return (
        True,
        f"Tool '{tool_name}' authorized."
    )