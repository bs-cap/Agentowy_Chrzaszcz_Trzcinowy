import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_ds
from .tools import check_products_in_db

load_dotenv()
model_name = os.getenv("MODEL")

# Tools (add the tool here when instructed)


# Agents

stock_checker_v1 = Agent(
    name="stock_checker_v1",
    model=model_name,
    description="Checking if product is in stock",
    instruction=return_instructions_ds(),
    tools = [check_products_in_db]
    )

stock_checker_v2 = Agent(
    name="stock_checker_v2",
    model=model_name,
    description="Checking if product is in stock",
    instruction=return_instructions_ds(),
    tools = [check_products_in_db]
    )