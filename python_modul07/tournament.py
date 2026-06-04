from typing import Callable
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, StrategyError, BattleStrategy
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory


def battle(opponents: list[tuple[Callable[[], Creature], BattleStrategy]]):

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            c1 = factory1()
            c2 = factory2()

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                if not strat1.is_valid(c1):
                    raise StrategyError(f"Invalid Creature '{c1.name}'")

                if not strat2.is_valid(c2):
                    raise StrategyError(f"Invalid Creature '{c2.name}'")

                print(strat1.act(c1, c2))
                print(strat2.act(c2, c1))

            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
        