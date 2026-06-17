from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ingredient = ingredients.lower()

    for item in allowed:

        if item in lower_ingredient:
            return ingredients + " - VALID"

    return ingredients + " - INVALID"
