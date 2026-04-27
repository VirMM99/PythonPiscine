
class Plant:
    def __init__(self, name: str, height: int, ages: int,) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self.ages = ages

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.ages += 1

    def get_info(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old"


rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)

print("=== Garden Plant Growth ===")

print(rose.get_info())
rose.grow()
rose.age()
initial_height = rose.height

for day in range(1, 8):
    print(f"=== Day {day} ===")
    print(rose.get_info())
    rose.grow()
    rose.age()

growth = round(rose.height - initial_height, 1)
print(f"Growth this week: {growth}cm")
