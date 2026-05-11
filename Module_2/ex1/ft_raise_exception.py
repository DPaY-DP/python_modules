def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    test_cases = ['25', 'abc', '100', '-50']

    for test in test_cases:
        print(f"Input data is '{test}'")
        try:
            temp = input_temperature(test)
            print(f"Temperature is now '{temp}'")
        except ValueError as error:
            # Catches wrong int() input
            print(f"Caught input_temperature error: {error}")
        except Exception as error:
            # Catches custom bounds errors
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
