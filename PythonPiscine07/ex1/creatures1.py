from abc import ABC, abstractmethod


class CreatureOne(ABC):
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type = type_

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(CreatureOne, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(CreatureOne, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(CreatureOne, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(CreatureOne, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
