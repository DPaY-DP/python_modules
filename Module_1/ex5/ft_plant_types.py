class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        if height < 0 or age < 0:
            print(f"{name.capitalize()}: Error height or "
                  "age can't be negative")
            return
        self.name = name
        self.height = height
        self.ageplant = age
        print(f"Plant created: {self.name.capitalize()}: "
              f"{round(self.height, 2)}cm,"
              f" {self.ageplant} days old")

    def show(self) -> None:
        return print("Current state: "
                     f"{self.name.capitalize()}: "
                     f"{round(self.height, 2)}cm, "
                     f"{self.ageplant} days old")

    def grow(self, add) -> None:
        self.height += add

    def age(self, add) -> None:
        self.ageplant += add

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.ageplant

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: "
                  "Error height or age can't be negative")
            print("Height update rejected")
        else:
            self.height = new_height
            print(f"Height updated: {new_height}")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: "
                  "Error height or age can't be negative")
            print("Age update rejected")
        else:
            self.ageplant = new_age
            print(f"Age updated: {new_age}")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, colour: str,
                 growth: float) -> None:
        super().__init__(name, height, age)
        self.colour = colour
        self.bloomed = 0
        self.growth = growth

    def bloom(self) -> None:
        self.bloomed = 1
        print(f"[asking the {self.name} to bloom]")
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Colour: {self.colour}")
        if self.bloomed == 0:
            return print(f" {self.name} has not bloomed yet")
        else:
            return print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.growth = growth

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.title()} now produces a shade of {self.height}"
              f"cm long and {self.trunk_diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth: float) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition_lvl = 0
        self.growth = growth

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.title()}")
        print(f" Nutritional value: {self.nutrition_lvl}")

    def grow_and_age(self, add) -> None:
        print(f"[make {self.name} grow and age for {add} days]")
        for i in range(0, add):
            super().grow(self.growth)
            super().age(1)
            self.nutrition_lvl += 1
        self.show()


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 34.0, 30, "red", 0.8)
    oak = Tree("Oak", 200.0, 10, 5.0, 5.0)
    tomato = Vegetable("tomato", 12.0, 15, "June", 0.3)
    print("=== Flower")
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    tomato.grow_and_age(20)


if __name__ == "__main__":
    main()
