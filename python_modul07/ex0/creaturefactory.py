from .creaturesall import Flameling, Pyrodon, Aquabub, Torragon
from .creature import Creature
from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Fire/Flaying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Water")

    def create_evolved(self) -> Creature:
        return Torragon("Water")
