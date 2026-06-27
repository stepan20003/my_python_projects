#!/usr/bin/env python3

from .battle_strategy import BattleStrategy, CreatureError
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament: "
                                f"Invalid Creature '{creature.name}' "
                                f"for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament: "
                                f"Invalid Creature '{creature.name}' "
                                f"for this aggressive strategy")
        trans = cast(TransformCapability, creature)
        print(trans.transform())
        print(creature.attack())
        print(trans.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament: "
                                f"Invalid Creature '{creature.name}' "
                                f"for this defensive strategy")
        heal = cast(HealCapability, creature)
        print(creature.attack())
        print(heal.heal())
