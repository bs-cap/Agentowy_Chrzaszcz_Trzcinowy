import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_sa
from .tools import get_weather

load_dotenv()
model_name = os.getenv("MODEL")

# Tools (add the tool here when instructed)


# Agents

supply_adviser = Agent(
    name="supply_adviser",
    model=model_name,
    description="Checking the stock if some of the products are out of stock. If so, send an email with order. Checking also the weather and prediction demand on products based on that",
    instruction=return_instructions_sa(),
    tools = [get_weather]
    )