

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.__height = float(height)
        self.__age = age
        print(f"Plant created: {self.name}:", end=' ')
        print(f"{self.__height}cm, {self.__age} days old")

    def __str__(self) -> str:
        return (
            f"Current state: {self.name}:"
            f" {round(self.get_height(), 1)}cm, {self.get_age()} days old"
        )

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, next_height: int) -> None:
        if next_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        elif next_height >= 0:
            print(f"Height updated: {next_height}cm")
            self.__height = float(next_height)

    def set_age(self, next_age: int) -> None:
        if next_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {next_age} days")
            self.__age = next_age


print("=== Garden Security System ===")
rose = SecurePlant("rose", 15, 10)
print()
rose.set_height(25)
rose.set_age(30)
print()
rose.set_height(-5)
rose.set_age(-5)
print()
print(rose)
