import asyncio

from mcp_server.server import mcp


async def main():
    print("MCP Server Created")
    print("Server Name:", mcp.name)

    print("\nRegistered MCP Tools:")

    tools = await mcp.list_tools()

    for tool in tools:
        print(tool.name)


if __name__ == "__main__":
    asyncio.run(main())