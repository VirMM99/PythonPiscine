
def ft_garden_intro(name: str, height: int, age: int) -> None:
    name = name.capitalize()
    if name:
        print(f"Plant: {name}")
    if height:
        print(f"Height: {height}cm")
    if age:
        print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_intro("rose", 25, 30)
    print()
    print("=== End of Program ===")
