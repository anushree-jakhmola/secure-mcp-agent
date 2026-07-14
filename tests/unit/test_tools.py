from mcp_server.registry import TOOL_REGISTRY

print("Registered Tools:")

for tool in TOOL_REGISTRY:
    print(tool)