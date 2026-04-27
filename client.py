from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"],
    # command="npx",
    # args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
)
async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                # TOOLS

                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool...")
                result = await session.call_tool("get_weather", arguments={"location": "San Francisco"})
                #result = await session.call_tool("airbnb_search", arguments={"location": "San Francisco"})
                print("Tool result:", result)

                
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())