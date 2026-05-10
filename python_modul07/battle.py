from ex0 import creaturefactory


def factory(obj: creaturefactory.CreatureFactory) -> None:
    print("Testing factory")
    flameling = obj.create_base()
    print(flameling.describe())
    print(flameling.attack())
    pyradon = obj.create_evolved()
    print(pyradon.describe())
    print(f"{pyradon.attack()}\n")


def battle(obj: creaturefactory.CreatureFactory,
           obj2: creaturefactory.CreatureFactory) -> None:
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
    factory(creaturefactory.FlameFactory())
    factory(creaturefactory.AquaFactory())
    battle(creaturefactory.FlameFactory(), creaturefactory.AquaFactory())
