# data_structures.py

def get_names(foods):
    """
    Retrieves names from a list of foods.

    Args:
    - foods (list): List of dictionaries representing foods.

    Returns:
    - list: List of names extracted from the input foods.
    """
    return [food['name'] for food in foods if 'name' in food]

def get_spiciest_foods(foods):
    """
    Retrieves the spiciest foods from a list of foods.

    Args:
    - foods (list): List of dictionaries representing foods.

    Returns:
    - list: List of the spiciest foods.
    """
    if not foods:
        return []

    spiciest_level = max(food.get('heat_level', 0) for food in foods)
    return [food for food in foods if food.get('heat_level', 0) == spiciest_level]

def print_spicy_foods(spicy_foods):
    """
    Prints the names of spicy foods.

    Args:
    - spicy_foods (list): List of dictionaries representing spicy foods.
    """
    for food in spicy_foods:
        print(food['name'])
