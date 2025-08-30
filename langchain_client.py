import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
load_dotenv()

llm = ChatOpenAI()

async def main():
    client = MultiServerMCPClient({
        "math":{
            "command" : "python",
            "args": [
                "/Users/thebinij/work_yipl/ai-agents-projects/mcp-server-learning/servers/math_server.py"
            ],
         "weather": {
             "url": "http://localhost:8000/sse",
             "transport": "sse",
         }
        }
    })

if __name__ == '__main__':
    asyncio.run(main())


