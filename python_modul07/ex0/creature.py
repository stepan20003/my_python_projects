from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{type(self).__name__} is a {self.name} type Creature"
