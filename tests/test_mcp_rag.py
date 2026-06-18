import asyncio

from mcp_server.server import mcp


async def main():

    result = await mcp.call_tool(
        "knowledge_base",
        {
            "query": "What is prompt injection?"
        }
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())