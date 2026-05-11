def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_cases = ['25', 'abc']

    for test in test_cases:
        print(f"Input data is '{test}'")
        try:
            temp = input_temperature(test)
            print(f"Temperature is now '{temp}'")
        except ValueError as error:
            # Catches wrong int() input
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
