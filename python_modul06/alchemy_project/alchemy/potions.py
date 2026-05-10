from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion():
    return (f"Healing potion brewed with’{create_earth()}’ and"
            f" ’{create_air()}'")


def strength_potion():
    return (f"Strength potion brewedwith '{create_fire()}'"
            f" and '{create_water()}'")
