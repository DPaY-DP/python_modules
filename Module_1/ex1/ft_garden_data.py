#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    # def __str__(self):
    #     return f"{self.name.capitalize()}: {self.height}cm, "
    #              + f"{self.age} days old")

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    Plant.show(rose)
    Plant.show(sunflower)
    Plant.show(cactus)
