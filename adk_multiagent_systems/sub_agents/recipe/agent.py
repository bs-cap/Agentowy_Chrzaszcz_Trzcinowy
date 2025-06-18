import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_rc
from .tools import extract_ingredients, exit_loop

from typing import List, Optional


load_dotenv()
model_name = os.getenv("MODEL")


# Agents

recipe_advertiser = Agent(
    name="recipe_advertiser",
    model=model_name,
    description="Creating recipe with given product",
    instruction=return_instructions_rc(),
    tools = [extract_ingredients, exit_loop]
    )