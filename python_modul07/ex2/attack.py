from .strategy import BattleStrategy, StrategyError
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature, opponent=None):
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature: Creature, opponent=None):
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        result = creature.revert()
        return result


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Creature, opponent=None):
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"defensive strategy"
            )

        print(creature.attack())
        hel = creature.heal()
        return hel
