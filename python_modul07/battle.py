from ex0 import FlameFactory, AquaFactory, CreatureFactory


def factory(obj: CreatureFactory) -> None:
    print("Testing factory")
    flameling = obj.create_base()
    print(flameling.describe())
    print(flameling.attack())
    pyradon = obj.create_evolved()
    print(pyradon.describe())
    print(f"{pyradon.attack()}\n")


def battle(obj: CreatureFactory,
           obj2: CreatureFactory) -> None:
    print("Testing battle")
    flameling = obj.create_base()
    print(flameling.describe())
    print(" vs.")
    aquabub = obj2.create_base()
    print(aquabub.describe())
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    factory(FlameFactory())
    factory(AquaFactory())
    battle(FlameFactory(), AquaFactory())
