

def validate_ingredients(ingredients: str):
    # Local import to avoid circular dependency
    from alchemy.grimoire.light_spellbook import (
        light_spell_allowed_ingredients
    )
    allowed = light_spell_allowed_ingredients()
    # Convert input string into list
    ingredients_list = ingredients.split(",")
    # Clean spaces
    ingredients_list = [i.strip() for i in ingredients_list]
    # Check validity
    if all(i in allowed for i in ingredients_list):
        return f"({ingredients.capitalize()} - VALID)"
    else:
        return f"({ingredients.capitalize()} - INVALID)"
