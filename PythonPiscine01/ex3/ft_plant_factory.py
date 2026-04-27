

class Plant:
    def __init__(
            self,
            name: str,
            starting_height: int,
            starting_age: int
            ) -> None:
        self.name = name.capitalize()
        self.starting_height = float(starting_height)
        self.starting_age = starting_age

    def show(self) -> str:
        return (
                f"Created: {self.name}: "
                f"{round(self.starting_height, 2)}cm, "
                f"{self.starting_age} days old"
        )


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    oak = Plant("oak", 200, 365)
    cactus = Plant("cactus", 5, 90)
    sunflower = Plant("sunflower", 80, 45)
    fern = Plant("fern", 15, 120)
    print("=== Plant Factory Output ===")
    print(rose.show())
    print(oak.show())
    print(cactus.show())
    print(sunflower.show())
    print(fern.show())

# list = [rose, oak, cactus, sunflower, fern]
# i = 0
# for plant_element in list:
#     i += 1
# print(f"\nTotal plants created: {i}")