import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_sa
from google.adk.tools.agent_tool import AgentTool
from .tools import get_weather, send_email
from sub_agents.stock.agent import stock_checker

load_dotenv()
model_name = os.getenv("MODEL")

# Tools (add the tool here when instructed)


# Agents

supply_adviser = Agent(
    name="supply_adviser",
    model=model_name,
    description="Supply Adviser",
    instruction=return_instructions_sa(),
    tools = [get_weather, AgentTool(agent=stock_checker),send_email]
    )