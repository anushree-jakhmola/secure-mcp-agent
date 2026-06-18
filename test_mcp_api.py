import inspect

from mcp.server.fastmcp import FastMCP

print("FastMCP imported successfully")
print("Class:", FastMCP)

methods = [
    name
    for name, _ in inspect.getmembers(FastMCP)
    if not name.startswith("_")
]

print("\nAvailable methods:")
for method in methods[:30]:
    print(method)