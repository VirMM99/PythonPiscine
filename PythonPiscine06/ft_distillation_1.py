

import alchemy


def heal():
    return alchemy.healing_potion()


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {alchemy.strength_potion()}")
print(f"Testing heal alias: {heal()}")
