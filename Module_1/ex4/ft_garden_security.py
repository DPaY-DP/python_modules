#!/usr/bin/env python3

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
        return "Current state: " \
               f"{self.name.capitalize()}: " \
               f"{round(self.height, 2)}cm, " \
               f"{self.ageplant} days old"

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


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 34.0, 30)
    print()
    rose.set_height(25.0)
    rose.set_age(28)
    print()
    rose.set_height(-4)
    rose.set_age(-4)
    print()
    print(rose.show())


if __name__ == "__main__":
    main()
