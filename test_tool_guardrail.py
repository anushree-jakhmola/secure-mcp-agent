from guardrails.tool_guardrails import authorize_tool

allowed, message = authorize_tool("system_info")

print("Allowed:", allowed)
print("Message:", message)

allowed, message = authorize_tool("delete_database")

print("Allowed:", allowed)
print("Message:", message)