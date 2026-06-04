from ex0.creaturefactory import CreatureFactory
from .creatures import Shiftling, Sproutling, Bloomelle, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Normal/Dragon")
