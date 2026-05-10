from .creaturesall import Flameling, Pyrodon, Aquabub, Torragon
from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling("Fire")

    def create_evolved(self):
        return Pyrodon("Fire/Flaying")


class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub("Water")

    def create_evolved(self):
        return Torragon("Water")
