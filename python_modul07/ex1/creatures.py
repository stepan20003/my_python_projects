from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{type(self).__name__} uses Vine Whip!"
    
    def heal(self) -> str:
        return f"{type(self).__name__} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{type(self).__name__} uses Petal Dance!"

    def heal(self) -> str:
        return (f"{type(self).__name__} heals itself and others for a large"
                f" amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.is_transformed = False

    def attack(self) -> str:
        if not self.is_transformed:
            return f"{type(self).__name__} attacks normally."
        else:
            return f"{type(self).__name__} performs a boosted strike!"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{type(self).__name__} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{type(self).__name__} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.is_transformed = False

    def attack(self) -> str:
        if not self.is_transformed:
            return f"{type(self).__name__} attacks normally."
        else:
            return (f"{type(self).__name__} unleashes a devastating "
                    f"morph strike!")

    def transform(self) -> str:
        self.is_transformed = True
        return f"{type(self).__name__} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{type(self).__name__} stabilizes its form."
