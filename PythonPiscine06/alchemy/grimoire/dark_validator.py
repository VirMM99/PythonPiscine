

from .dark_spellbook import (dark_spell_allowed_ingredients)


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    # Convert input string into list
    ingredients_list = ingredients.split(",")
    # Clean spaces
    ingredients_list = [i.strip() for i in ingredients_list]
    # Check validity
    if all(i in allowed for i in ingredients_list):
        return f"{ingredients} -> VALID"
    else:
        return f"{ingredients} - INVALID"
