class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water:")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    garden = ["Tomato", "Lettuce", "Carrots"]
    garden_error = ["Tomato", "lettuce", "carrots"]

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for test in garden:
            water_plant(test)
            print(f"Watering {test}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e} {test}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for test in garden_error:
            water_plant(test)
            print(f"Watering {test}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e} {test}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
