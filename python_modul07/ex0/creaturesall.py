from creature import Creature


class Flameling(Creature):
    def attack(self) -> str:
        return "Ember"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Flamethrower"


class Aquabub(Creature):
    def attack(self):
        return "Water Gun"


class Torragon(Creature):
    def attack(self):
        return "Hydro Pump"
