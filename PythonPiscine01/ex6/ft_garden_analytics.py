

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def increase_grow(self) -> None:
            self._grow += 1

        def increase_age(self) -> None:
            self._age += 1

        def increase_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow} grow,"
                f" {self._age} age,"
                f" {self._show} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age_days
        self._stats = Plant._Stats()

    # STATIC METHOD
    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    # CLASS METHOD
    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: int) -> None:
        self.height += amount
        self._stats.increase_grow()

    def age(self, days: int) -> None:
        self.age_days += days
        self._stats.increase_age()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        self._stats.increase_show()

    def display_stats(self) -> None:
        self._stats.display()


# FLOWER
class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str
            ) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# SEEDS(Hereda de FLOWER)
class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str
            ) -> None:
        super().__init__(name, height, age_days, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


# TREE
class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def increase_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )
        self._stats.increase_shade()  # type: ignore

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


# GLOBAL FUNCTION
def display_stats(plant: Plant) -> None:
    plant.display_stats()


# MAIN TEST
if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print(
        "Is 400 days more than a year? ->",
        Plant.is_older_than_year(400)
        )
    print()
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("make sunflower grow, age and bloom")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)
