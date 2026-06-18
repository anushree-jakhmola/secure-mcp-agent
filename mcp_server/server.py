"""
Secure Tool Executor

All tool invocations pass through this layer.
"""

from guardrails.tool_guardrails import authorize_tool
from mcp_server.registry import TOOL_REGISTRY


def execute_tool(tool_name: str):
    """
    Secure tool execution workflow.

    1. Authorize tool
    2. Lookup tool
    3. Execute tool
    """

    allowed, message = authorize_tool(tool_name)

    if not allowed:
        raise PermissionError(message)

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        raise ValueError(
            f"Tool '{tool_name}' not found in registry."
        )

    return tool()