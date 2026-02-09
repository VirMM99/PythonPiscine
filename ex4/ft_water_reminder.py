
def ft_water_reminder():
    water_reminder = int(input("Days since last watering: "))
    if (water_reminder > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
