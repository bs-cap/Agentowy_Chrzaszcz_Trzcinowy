import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from google.genai import types
from .prompts import return_instructions_rc
from google.adk.tools.agent_tool import AgentTool
from .tools import extract_ingredients, exit_loop
from google.adk.tools import google_search

from typing import List, Optional


load_dotenv()
model_name = os.getenv("MODEL")


# Agents

search_agent = Agent(
    name="basic_search_agent",
    model=model_name,
    description="Agent to find recipe with given product",
    instruction="Look for one short recipe with given product",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)


recipe_advertiser = Agent(
    name="recipe_advertiser",
    model=model_name,
    description="Searching for a recipe with given product",
    instruction=return_instructions_rc(),
    tools = [AgentTool(agent=search_agent), extract_ingredients, exit_loop],
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    )
    )