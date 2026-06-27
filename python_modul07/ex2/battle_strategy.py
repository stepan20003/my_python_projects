#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature


class CreatureError(Exception):
    def __init__(self, err_str: str) -> None:
        super().__init__(err_str)


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass
