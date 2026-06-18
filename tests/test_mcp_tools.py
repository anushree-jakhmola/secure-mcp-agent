import asyncio

from mcp_server.server import mcp


async def main():

    tools = await mcp.list_tools()

    print(
        "\nRegistered MCP Tools:\n"
    )

    for tool in tools:
        print(tool.name)


if __name__ == "__main__":
    asyncio.run(main())