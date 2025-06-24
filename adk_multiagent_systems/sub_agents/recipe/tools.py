from typing import List, Dict, Any
from google.adk.tools.tool_context import ToolContext

def extract_ingredients(recipe: Dict[str, Any]) -> List[str]:
    """
    Tool: Ingredient Extractor

    Description:
    This function takes a recipe represented as a dictionary and extracts all unique 
    ingredients into a list. It handles nested structures and returns a clean, deduplicated 
    list of ingredient names.

    Parameters:
    - recipe (Dict[str, Any]): A dictionary representing the recipe. The dictionary should 
      have an 'ingredients' field containing a list of ingredient dictionaries.

    Returns:
    - List[str]: A list of unique ingredient names.
    """
    ingredients_set = set()

    if 'ingredients' in recipe:
        for ing in recipe['ingredients']:
            if 'ingredient' in ing:
                ingredients_set.add(ing['ingredient'])

    return list(ingredients_set)


def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when 'stock_checker' agent approve that all ingredients are in stock."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}


if __name__ == "__main__":
    print(extract_ingredients({'description': 'A simple and healthy banana smoothie.', 'name': 'Banana Smoothie', 'servings': 1, 'instructions': ['Combine all ingredients in a blender.', 'Blend until smooth.', 'Pour into a glass and serve immediately.'], 'ingredients': [{'unit': 'piece', 'ingredient': 'banana', 'quantity': '1'}, {'quantity': '1', 'unit': 'cup', 'ingredient': 'milk'}, {'unit': 'tablespoon', 'quantity': '1', 'ingredient': 'honey'}], 'prep_time': '5 minutes', 'cook_time': '0 minutes'}))


