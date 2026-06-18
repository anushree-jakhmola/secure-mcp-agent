"""
Secure MCP Server

All MCP tool requests are routed
through the Secure Tool Executor.
"""

from mcp.server.fastmcp import FastMCP

from guardrails.tool_guardrails import authorize_tool
from mcp_server.registry import TOOL_REGISTRY
from guardrails.audit_logger import log_event

mcp = FastMCP("Secure MCP Agent")


def execute_tool(tool_name: str, *args, **kwargs):
    """
    Centralized secure execution.
    """

    allowed, message = authorize_tool(tool_name)

    if not allowed:
        raise PermissionError(message)

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        raise ValueError(
            f"Tool '{tool_name}' not found."
        )

    result = tool(
        *args,
        **kwargs
    )

    log_event(
        "TOOL_EXECUTED",
        tool_name,
    )

    return result


@mcp.tool()
def system_info():
    """
    Return safe system information.
    """

    return execute_tool("system_info")


@mcp.tool()
def knowledge_base(
    query: str
):
    """
    Search security knowledge base.
    """

    return execute_tool(
        "knowledge_base",
        query
    )


if __name__ == "__main__":
    mcp.run()