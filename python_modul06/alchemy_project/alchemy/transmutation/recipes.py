from alchemy import potions


def lead_to_gold():
    return (f"Recipe transmuting Lead to Gold: brew ’{potions.create_air()}’ "
            f"and ’{potions.strength_potion()}’ mixed with "
            f"’{potions.create_fire()}’")
