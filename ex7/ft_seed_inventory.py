
def ft_seed_inventory(seed_type: str, quantity: int,
                      unit: str) -> None:
    if (seed_type == "tomato" or seed_type == "carrot"):
        print(f"{seed_type.capitalize()} seeds:", end=" ")
        print(f"{quantity}", end=" ")
    elif seed_type == "lettuce":
        print(f"{seed_type.capitalize()} seeds: covers", end=" ")
        print(f"{quantity}", end=" ")
    if unit == "packets":
        print("packets available")
    elif unit == "grams":
        print("grams total")
    elif unit == "area":
        print("square meters")
    else:
        print("Unknown unit type")
