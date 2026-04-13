
class Plant:
    class __Stats:
        def __init__(self):
            self.age_calls = 0
            self.grow_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

        def display(self, plant):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls}"
                  f"age, {self.show_calls} show")
            if plant.__class__.__name__ == "Tree":
                print(f"{self.shade_calls} shade")

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.__Stats()

    def show(self, first=True):
        if first:
            if self.name == "Unknown":
                print("=== Anonymous")
            else:
                print(f"=== {self.__class__.__name__}")
        print(f"{self.name}: {round(self.height,1)}cm, {self.age} days old")
        self._stats.show_calls += 1

    @staticmethod
    def is_valid_year(year: int):
        print("=== Check year-old")
        if year >= 365:
            print(f"Is {year} days more than a year? -> True")
        else:
            print(f"Is {year} days more than a year? -> False")

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.ftbloom = 0
        self.seeds = 0

    def bloom(self):
        self.ftbloom = 1

    def show(self, first=True):
        super().show(first)
        print(f"Color: {self.color}")
        if self.ftbloom == 1:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def grow(self, n: int):
        self.height += n
        self._stats.grow_calls += 1

    def age_plant(self, x: int):

        self.age += x
        self._stats.age_calls += 1
        self.seeds += x * 2.1


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)

    def show(self, first=True):
        super().show(first)
        print(f"{int(self.seeds)}")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm "
              f"long and {self.diameter}cm wide")
        self._stats.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def grow(self, n: int):
        self.height += n
        self._stats.grow_calls += 1

    def age_plant(self, n: int):
        self.age += n
        self._stats.age_calls += 1


if __name__ == "__main__":

    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Garden statistics ===")
    Plant.is_valid_year(30)
    Plant.is_valid_year(400)
    print("\n")
    rose.show()
    print("[statistics for Rose]")
    rose._stats.display(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8)
    rose.show(first=False)
    print("[statistics for Rose]")
    rose._stats.display(rose)
    print("\n")
    oak.show()
    print("[statistics for Oak]")
    oak._stats.display(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak._stats.display(oak)
    print("\n")
    seed.show()
    print("[make sunflower grow,age and bloom]")
    seed.grow(30)
    seed.age_plant(20)
    seed.bloom()
    seed.show(first=False)
    print("[statistics for Sunflower]")
    seed._stats.display(seed)
    print("\n")
    p = Plant.anonymous()
    p.show()
    print("[statistics for Unknown plant]")
    p._stats.display(p)
