def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        return print("Plant is rady to harvest!")
    else:
        return print("Plant needs more time to grow.")
