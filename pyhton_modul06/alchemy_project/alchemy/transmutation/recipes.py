from alchemy import potions
def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew ’{potions.create_air()}’ and ’{potions.strength_potion()}’ mixed with ’{potions.create_fire()}’"