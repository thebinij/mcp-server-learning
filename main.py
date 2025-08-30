import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()


stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/thebinij/work_yipl/ai-agents-projects/mcp-server-learning/servers/math_server.py"]
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")

            tools = await load_mcp_tools(session) ## convert tools mcp tools to langchain tools

            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 14 + 23  ?")]}
            )

            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())