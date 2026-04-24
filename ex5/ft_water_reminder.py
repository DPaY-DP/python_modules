def ft_water_reminder():
    last_watered = int(input("Days since last watering: "))
    if last_watered > 2:
        return print("Water the plants!")
    else:
        return print("Plants are fine")
