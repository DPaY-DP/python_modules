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

    def show(self) -> str:
        return print("Current state: " 
                    f"{self.name.capitalize()}: "
                    f"{round(self.height, 2)}cm, "
                    f"{self.ageplant} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.ageplant += 1

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
    def __init__(self, name: str, height: int, age: int, colour: str) -> None:
        super().__init__(name, height, age)
        self.colour = colour
        self.bloomed = 0

    def bloom(self) -> None:
        self.bloomed = 1
        return print(f"[asking the {self.name} to bloom]")
    
    def show(self) -> None:
        super().show()
        print(f"Colour: {self.colour}")
        if self.bloomed == 0:
            return print(f"{self.name} has not bloomed yet")
        else:
            return print(f"{self.name} is blooming beautifully!")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 34.0, 30, "red")
    rose.show()
    rose.bloom()
    rose.show()
    


if __name__ == "__main__":
    main()