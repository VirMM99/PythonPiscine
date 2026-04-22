

def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    from alchemy.grimoire.light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} {result}"
    else:
        return f"Spell '{spell_name}' rejected due to invalid ingredients"
