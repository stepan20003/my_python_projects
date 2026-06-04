from .strategy import BattleStrategy, StrategyError
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability

class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature, opponent=None):
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature, opponent=None):

        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        return creature.revert()


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature, opponent=None):

        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )

        print(creature.attack())
        return creature.heal()
