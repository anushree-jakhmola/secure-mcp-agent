"""
Central security policy for the Secure MCP Agent.

All guardrails and tool authorization decisions
should reference this file.
"""

ALLOWED_TOOLS = {
    "knowledge_base",
    "policy_lookup",
    "file_access",
    "system_info",
}

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden prompt",
    "act as root",
    "bypass restrictions",
    "disable guardrails",
]

ALLOWED_FILE_DIRECTORY = "knowledge_base/docs"