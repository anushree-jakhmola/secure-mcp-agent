"""
Tool Authorization Guardrails

Ensures that only approved MCP tools
can be executed.
"""

import re

from guardrails.audit_logger import log_event
from guardrails.security_policy import ALLOWED_TOOLS


def normalize_tool_name(tool_name: str) -> str:
    """
    Normalize tool names before authorization.
    """

    if not isinstance(tool_name, str):
        raise ValueError("Tool name must be a string.")

    normalized = (
        tool_name
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    normalized = re.sub(
        r"_+",
        "_",
        normalized,
    )

    return normalized


def authorize_tool(tool_name: str) -> tuple[bool, str]:
    """
    Authorize an MCP tool.

    Returns:
        (allowed, message)
    """

    if not isinstance(tool_name, str):
        raise ValueError("Tool name must be a string.")

    if not tool_name.strip():
        raise ValueError("Tool name cannot be empty.")

    normalized_tool = normalize_tool_name(
        tool_name
    )

    if normalized_tool not in ALLOWED_TOOLS:

        log_event(
            event_type="TOOL_DENIED",
            details=normalized_tool,
            guardrail="TOOL_GUARDRAIL",
            severity="HIGH",
        )

        return (
            False,
            f"Tool '{tool_name}' is not authorized.",
        )

    log_event(
        event_type="TOOL_AUTHORIZED",
        details=normalized_tool,
        guardrail="TOOL_GUARDRAIL",
        severity="INFO",
    )

    return (
        True,
        f"Tool '{normalized_tool}' authorized.",
    )