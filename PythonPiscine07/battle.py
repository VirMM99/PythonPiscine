from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2):
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print("Testing battle")
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("figth!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    battle(flame, aqua)
