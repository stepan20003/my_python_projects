class Plant:
    def __init__(self, name, height, age):

        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = height
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age
        print(f"Plant created: {self.name}: {round(self._height,1)}"
              f"cm, {self._age} days old")

    def show(self):
        print(f"{self.name}: {round(self._height,1)}cm, {self._age} days old")

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def get_height(self):
        return self._height

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-1)
    print("Current state: ", end=" ")
    rose.show()
