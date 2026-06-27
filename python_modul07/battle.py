#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()}\n vs.\n{c2.describe()}\n fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    print("Testing factory")
    test_factory(flame)
    print()
    print("Testing factory")
    test_factory(aqua)
    print()
    print("Testing battle")
    test_battle(flame, aqua)
