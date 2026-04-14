class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.count = 0.0
        self.day = 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.age} days old")
        if self.day != 8:
            print(f"=== Day {self.day} ===")

    def grow(self) -> None:
        self.height = self.height + 0.8
        self.count += 0.8

    def age_one(self) -> None:
        self.age += 1
        self.day += 1


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    Rose.show()
    for _ in range(7):
        Rose.age_one()
        Rose.grow()
        Rose.show()
    print(f"Growth this week: {Rose.count}cm")
