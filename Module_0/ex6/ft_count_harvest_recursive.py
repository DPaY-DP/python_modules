def ft_helper_recursive(number):
    if number > 1:
        number -= 1
        ft_helper_recursive(number)
        return print(f"Day {number}")


def ft_count_harvest_recursive():
    number = int(input("Days until harvest: "))
    if number != 1:
        number += 1
        ft_helper_recursive(number)
    return print("Harvest time!")
