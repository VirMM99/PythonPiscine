
def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def counting_days(day):
        print(f"Day {day}")
        if day == harvest:
            print("Harvest time!")
            return
        counting_days(day + 1)

    counting_days(1)
