# autonomous_agent.py

import os
import time
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
from tools.swap import swap_tokens
from tools.price import get_token_price

load_dotenv()

# Load Groq LLM
llm = ChatGroq(
    temperature=0.3,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

# Strategy function for the bot to execute

def auto_strategy(_):
    try:
        print("\n🧠 Strategy: Swap 5 USDC to DAI")
        return swap_tokens("USDC", "DAI", 5)
    except Exception as e:
        return f"❌ Strategy failed: {e}"

# Register tools for LangChain agent
tools = [
    Tool(name="Swap Tokens", func=auto_strategy, description="Executes a swap using the Recall sandbox API"),
    Tool(name="Get Token Price", func=get_token_price, description="Fetches token price from CoinGecko")
]

# Initialize LangChain agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Loop runner
def run_autonomous_agent():
    while True:
        try:
            print("\n💬 Thinking...")
            response = agent.run("Run your trading strategy.")
            print(f"\n🤖 Response: {response}")
        except Exception as e:
            print(f"\n❌ Agent error: {e}")

        print("\n⏱️ Waiting 1800 seconds (30 minutes) before next action...\n")
        time.sleep(1800)  # Run every 30 minutes

# Start the agent
if __name__ == "__main__":
    run_autonomous_agent()
