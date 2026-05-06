#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    # def __str__(self):
    #     return f"{self.name.capitalize()}: {self.height}cm, "
    #              + f"{self.age} days old")

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 2)}cm, "
              f"{self.age} days old")
    
    def grow(self):
        self.height += 0.8
        
    def age(self):
        self.age += 1

def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Plant.show(rose)
        Plant.grow(rose)
        Plant.age(rose)

if __name__ == "__main__":
    main()
