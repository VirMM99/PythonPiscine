from typing import Any
from abc import ABC, abstractmethod
from ex1.creatures1 import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    # Validate if that creature can use that estragedy
    def is_valid(self, creature: Any) -> bool:
        pass

    # Execute the action in battle
    @abstractmethod
    def act(self, creature: Any) -> None:
        pass


class NormalStrategy(BattleStrategy):
    # NormalStrategy, suitable for any Creature
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise Exception(
                            f"Invalid Creature '{creature.name}'"
                            "for this normal strategy"
                            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise Exception(
                            f"Invalid Creature '{creature.name}'"
                            "for this aggressive strategy"
                            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise Exception(
                            f"Invalid Creature '{creature.name}'"
                            "for this defensive strategy"
                            )
        print(creature.attack())
        print(creature.heal())
