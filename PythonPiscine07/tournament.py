from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def tournament(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    # evita duplicados y autobatallas
    for i in range(len(opponents)):
        for k in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[k]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def format_opponents(opponents):
    names = []
    for factory, strategy in opponents:
        factory_name = factory.__class__.__name__.replace("Factory", "")
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")
        names.append(f"({factory_name} + {strategy_name})")
    return "[" + ", ".join(names) + "]"


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(format_opponents(opponents))
    tournament(opponents)
    print()
    print("Tournament 1 (error)")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),  # No va a poder tranformarse
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(format_opponents(opponents))
    tournament(opponents)
    print()
    print("Tournament 2 (multiple)")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print(format_opponents(opponents))
    tournament(opponents)
