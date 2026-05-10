from .creature import Creature


class Flameling(Creature):
    def attack(self) -> str:
        return f"{type(self).__name__} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{type(self).__name__} uses Flamethrower!"


class Aquabub(Creature):
    def attack(self):
        return f"{type(self).__name__} uses Water Gun!"


class Torragon(Creature):
    def attack(self):
        return f"{type(self).__name__} uses Hydro Pump!"
