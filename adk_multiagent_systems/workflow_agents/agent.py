import os
import logging
import google.cloud.logging

from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent
from google.genai import types
from sub_agents.stock.agent import stock_checker
from sub_agents.recipe.agent import recipe_advertiser
from sub_agents.supply.agent import supply_adviser
from sub_agents.promoter.agent import promoter



load_dotenv()

model_name = os.getenv("MODEL")
print(model_name)

recipe_loop = LoopAgent(
    name="RecipeLoopAgent",
    sub_agents=[
        recipe_advertiser,
        stock_checker,
    ],
    max_iterations=3 # Limit loops
)

#create sequential agent with promotororkspace ~
prom_seq = SequentialAgent(
    name = 'prom_seq',
    sub_agents = [
        recipe_loop,
        promoter
    ]
)
root_agent = Agent(
    name="manager",
    model=model_name,
    description="Marketing manager",
    instruction="""
    When the user provide some information about recipe delegate that task to 'prom_seq' agent 
    Otherwise when you get some information about supply delegate that task to 'supply_adviser' agent input must be provided by user !!.
    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    sub_agents=[prom_seq, supply_adviser]
)
