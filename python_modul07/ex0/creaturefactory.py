from creaturesall import Flameling,Pyrodon,Aquabub,Torragon
from abc import ABC,abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base():
        pass

    @abstractmethod
    def create_evolved():
        pass


class FlameFactory(CreatureFactory):
    def create_base():
        obj = Flameling("Fire")

