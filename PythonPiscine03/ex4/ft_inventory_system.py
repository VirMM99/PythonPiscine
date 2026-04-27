

import sys


def main() -> None:
    # Scrip name is [0] sys.argv[1:] is where real data starts
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")
    # All the Parsing
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item: str
        quantity_str: str
        item, quantity_str = arg.split(":", 1)
        # Discarding duplicates
        if item in inventory:
            print((f"Redundant item '{item}' - discarding"))
            continue
        try:
            quantity = int(quantity_str)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inventory[item] = quantity
    # Display for Inventory
    print(f"Got inventory: {inventory}")
    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    # This is for the percentages
    for item in inventory:
        percent: float = (inventory[item] / total) * 100
        print(f"Item {item} represents {round(percent, 1)}%")
    # The Most and the Least. Equal to None bcoz we dont have a value yet
    max_item: str = items[0]
    min_item: str = items[0]
    for item in inventory:
        if max_item is None or inventory[item] > inventory[max_item]:
            max_item = item
        if min_item is None or inventory[item] < inventory[min_item]:
            min_item = item
    print(
        f"Item most abundant: {max_item} with quantity "
        f"{inventory[max_item]}")
    print(
        f"Item least abundant: {min_item} with quantity "
        f"{inventory[min_item]}")
    # For adding new item
    inventory.update({"magic_item": 1})
    print(f"Update inventory: {inventory}")


if __name__ == '__main__':
    main()
