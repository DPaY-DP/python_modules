class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        if height < 0 or age < 0:
            print(f"{name.capitalize()}: Error height or "
                  "age can't be negative")
            return
        self.name = name
        self.__height = height
        self.__age = age
        self.stats = self.Stats()
        print(f"Plant created: {self.name.capitalize()}: "
              f"{round(self.__height, 2)}cm,"
              f" {self.__age} days old")

    @classmethod
    def create_anonymous(cls):
        """Creating an instance without having every info"""
        return cls("Unknown plant", 0.0, 0)
        
    
    class Stats():
        def __init__(self):
            self._grow_stat = 0
            self._age_stat = 0
            self._show_stat = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_stat} grow, "
              f"{self._age_stat} age, "
              f"{self._show_stat} show")

    def show(self) -> None:
        self.stats._show_stat += 1
        print("Current state: "
              f"{self.name.capitalize()}: "
              f"{round(self.__height, 2)}cm, "
              f"{self.__age} days old")

    def grow(self, add) -> None:
        self.__height += add
        self.stats._grow_stat += 1

    def age(self, add) -> None:
        self.__age += add
        self.stats._age_stat += 1

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: "
                  "Error height or age can't be negative")
            print("Height update rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: "
                  "Error height or age can't be negative")
            print("Age update rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age}")

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False


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
            return print(f" {self.name.title()} has not bloomed yet")
        else:
            return print(f" {self.name.title()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth: float) -> None:
        super().__init__(name, height, age)
        self.stats = self.Stats()
        self.trunk_diameter = trunk_diameter
        self.growth = growth

    class Stats(Plant.Stats):
            def __init__(self):
                super().__init__()
                self._produce_shade_stat = 0
            
            def display(self) -> None:
                print(f"Stats: {self._grow_stat} grow, "
                      f"{self._age_stat} age, "
                      f"{self._show_stat} show")
                print(f"{self._produce_shade_stat} shade")

    def produce_shade(self) -> None:
        self.stats._produce_shade_stat += 1
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.title()} now produces a shade of {self.get_height()}"
              f"cm long and {self.trunk_diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, colour: str,
                 growth: float, seed_number: int) -> None:
        super().__init__(name, height, age, colour, growth)
        self._seed_count = seed_number

    def show(self) -> None:
        super().show()
        if self.bloomed == 0:
            print(f"Seeds: 0")
        else:
            print(f"Seeds: {self._seed_count}")

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


def display_plant_stats(plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()

def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 34.0, 30, "red", 0.8)
    oak = Tree("Oak", 200.0, 10, 5.0, 5.0)
    tomato = Vegetable("tomato", 12.0, 15, "June", 0.3)
    unknown = Plant.create_anonymous()
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 0.2, 42)
    agetest = [30, 400]
    garden = [rose, oak, sunflower, unknown]
    print()
    print("=== Check year-old")
    for i in agetest:
        if Plant.check_age(i) == True:
            print(f"Is {i} days more than a year? -> True")
        else:
            print(f"Is {i} days more than a year? -> False")
    print()
    for i in garden:
        if i == rose:
            print("=== Flower")
            i.show()
            display_plant_stats(i)
            i.bloom()
            display_plant_stats(i)
        elif i == oak:
            print("=== Tree")
            i.show()
            display_plant_stats(i)
            i.produce_shade()
            display_plant_stats(i)
        elif i == sunflower:
            print("=== Seed")
            i.show()
            display_plant_stats(i)
            i.bloom()
            display_plant_stats(i)
        else:
            print("=== Anonymous")
            i.show()
            display_plant_stats(i)
        print()


if __name__ == "__main__":
    main()
