from ex0.creaturefactory import CreatureFactory
from ex0.creature import Creature
from .creatures import Shiftling, Sproutling, Bloomelle, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Grass")

    def create_evolved(self):
        return Bloomelle("Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Normal")

    def create_evolved(self):
        return Morphagon("Normal/Dragon")
