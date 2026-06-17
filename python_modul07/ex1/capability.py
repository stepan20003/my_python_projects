from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
