import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_pr

from typing import List, Optional


load_dotenv()
model_name = os.getenv("MODEL")


# Agents

promoter = Agent(
    name="promoter",
    model=model_name,
    description="Creating promotion or displaying recipe with given product",
    instruction=return_instructions_pr(),
    )