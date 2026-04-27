

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color_attribute: str
            ) -> None:
        super().__init__(name, height, age)
        self.color_attribute = color_attribute
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color_attribute}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of", end=' ')
        print(
                f"{round(self.height, 1)}cm long and "
                f"{round(self.trunk_diameter, 1)}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm: int) -> None:
        self.height += cm
        self.nutritional_value += cm

    def age_one_day(self, days: int) -> None:
        self.age += days
        self.nutritional_value = days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


rose = Flower("rose", 15, 10, "red")
kala = Flower("kala", 25, 30, "white")
oak = Tree("oak", 200, 365, 5)
olive = Tree("olive", 900, 3652, 150)
tomato = Vegetable("tomato", 5, 10, "April")
carrot = Vegetable("carrot", 80, 90, "spring")
print("=== Garden Plant Types ===")
print("== Flower")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()
print()
print("== Tree")
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print()
print("== Vegetable")
tomato.show()
print("[make tomato grow and age for 20 days]")
tomato.grow(42)
tomato.age_one_day(20)
tomato.show()
