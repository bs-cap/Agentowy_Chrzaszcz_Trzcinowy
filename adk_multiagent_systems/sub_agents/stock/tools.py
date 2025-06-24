import sqlite3
from typing import List, Dict

def check_products_in_db(product_list: List[str], db_path: str = 'sub_agents/stock/inventory.db') -> Dict[str, bool]:
    """
    Agent Tool: Product Availability Checker

    Description:
    This function serves as a tool for the `stock_checker` agent. It verifies the existence of 
    specified product names within the 'products' table of a SQLite database. It is typically 
    invoked by agents such as `recipe_advertiser` or `supply_adviser` to confirm inventory status 
    before proceeding with recipe publication or supply recommendations.

    Parameters:
    - product_list (List[str]): A list of product names to check for existence in the database.
    - db_path (str): The path to the SQLite database file. Default is 'inventory.db'.

    Returns:
    - Dict[str, bool]: A dictionary mapping each product name to a boolean indicating whether 
      it exists in the database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    product_existence = {}

    for product in product_list:
        cursor.execute("SELECT EXISTS(SELECT 1 FROM products WHERE name=?)", (product,))
        exists = cursor.fetchone()[0]
        product_existence[product] = bool(exists)

    conn.close()
    return product_existence

if __name__ == "__main__": 
    product_list = ['apple', 'banana', 'orange']
    print(check_products_in_db(product_list))

