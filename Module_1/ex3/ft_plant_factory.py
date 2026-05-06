#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.ageplant = age
    #     return f"{self.name.capitalize()}: {self.height}cm, "
    #              + f"{self.age} days old")

    def show(self) -> str:
        return f"{self.name.capitalize()}: {round(self.height, 2)}cm, " \
                    f"{self.ageplant} days old"

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.ageplant += 1

    def calc_height(self) -> float:
        return self.height


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("sunflower", 110.0, 100)
    oak = Plant("oak", 270.0, 3600)
    cactus = Plant("cactus", 4.0, 50)
    fern = Plant("fern", 1.0, 2)
    print("=== Plant Factory Ouput ===")
    print(f"Created: {rose.show()}")
    print(f"Created: {sunflower.show()}")
    print(f"Created: {oak.show()}")
    print(f"Created: {cactus.show()}")
    print(f"Created: {fern.show()}")


if __name__ == "__main__":
    main()
