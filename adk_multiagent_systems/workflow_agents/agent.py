import os
import logging
import google.cloud.logging

from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent
from google.genai import types
from sub_agents.stock.agent import stock_checker_v1, stock_checker_v2
from sub_agents.recipe.agent import recipe_advertiser
from sub_agents.supply.agent import supply_adviser



load_dotenv()

model_name = os.getenv("MODEL")
print(model_name)

supply_loop = LoopAgent(
    name="SupplyLoopAgent",
    sub_agents=[
        supply_adviser,
        stock_checker_v1,
    ],
    max_iterations=1# Limit loops
)

recipe_loop = LoopAgent(
    name="RecipeLoopAgent",
    sub_agents=[
        recipe_advertiser,
        stock_checker_v2,
    ],
    max_iterations=3 # Limit loops
)

root_agent = Agent(
    name="manager",
    model=model_name,
    description="Marketing manager",
    instruction="""
    When the user provide some information about recipe delegate that task to 'RecipeLoopAgent' agent 
    Otherwise when you get some information about supply delegate that task to 'SupplyLoopAgent' agent input must be provided by user !!.
    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    sub_agents=[recipe_loop, supply_loop]
)
