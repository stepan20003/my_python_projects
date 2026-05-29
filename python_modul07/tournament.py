from ex2 import (NormalStrategy, AggressiveStrategy, DefensiveStrategy,
                 StrategyError, BattleStrategy)
from ex0 import CreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
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
                a = strat2.__class__.__name__.replace('Strategy', '').lower()
                a += ' strategy'
                b = strat1.__class__.__name__.replace('Strategy', '').lower()
                b += ' strategy'
                if not strat1.is_valid(c1):
                    raise StrategyError(f"Invalid Creature "
                                        f"'{type(c1).__name__}' for this {b}")

                if not strat2.is_valid(c2):
                    
                    raise StrategyError(f"Invalid Creature "
                                        f"'{type(c1).__name__}' for this {a}")

                print(strat1.act(c1, c2))
                print(strat2.act(c2, c1))

            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    from ex1 import HealingCreatureFactory, TransformCreatureFactory
    from ex0 import FlameFactory, AquaFactory
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    Sproutling = HealingCreatureFactory()
    Shiftling = TransformCreatureFactory()
    Flameling = FlameFactory()
    Aquabub = AquaFactory()
    battle([
        (Flameling.create_base, NormalStrategy()),
        (Sproutling.create_base, DefensiveStrategy()),
    ])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (Flameling.create_base, AggressiveStrategy()),
        (Sproutling.create_base, DefensiveStrategy()),
    ])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (Aquabub.create_base, NormalStrategy()),
        (Sproutling.create_base, DefensiveStrategy()),
        (Shiftling.create_base, AggressiveStrategy()),
    ])
