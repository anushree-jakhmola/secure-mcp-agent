import asyncio

from mcp_server.server import mcp


async def main():
    result = await mcp.call_tool(
        "system_info",
        {}
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())