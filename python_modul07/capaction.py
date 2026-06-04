from ex1 import (CreatureFactory, TransformCreatureFactory,
                 HealingCreatureFactory)


def healing(obj: CreatureFactory | HealingCreatureFactory) -> None:
    sproulting = obj.create_base()
    print("Testing Creature with healing capability")
    print(" base:")
    print(sproulting.describe())
    print(sproulting.attack())
    print(sproulting.heal())
    print(" evolved:")
    bloomele = obj.create_evolved()
    print(bloomele.describe())
    print(bloomele.attack())
    print(bloomele.heal())


def transforms(obj: CreatureFactory | TransformCreatureFactory) -> None:
    shiftling = obj.create_base()
    print("\nTesting Creature with transform capability")
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print(" envolved:")
    morphagon = obj.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


if __name__ == "__main__":
    healing(HealingCreatureFactory())
    transforms(TransformCreatureFactory())