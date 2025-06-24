import os
import sys
sys.path.append("..")
from dotenv import load_dotenv
from google.adk import Agent
from .prompts import return_instructions_ds
from .tools import check_products_in_db

load_dotenv()
model_name = os.getenv("MODEL")


stock_checker = Agent(
    name="stock_checker",
    model=model_name,
    description="Checking if product is in stock",
    instruction=return_instructions_ds(),
    tools = [check_products_in_db]
    )