from abc import ABC, abstractmethod
from .creatures1 import (
                        CreatureOne, Sproutling, Bloomelle,
                        Shiftling, Morphagon
                        )


class CreatureFactoryOne(ABC):
    @abstractmethod
    def create_base(self) -> CreatureOne:
        pass

    @abstractmethod
    def create_evolved(self) -> CreatureOne:
        pass


class HealingCreatureFactory(CreatureFactoryOne):
    def create_base(self) -> CreatureOne:
        return Sproutling()

    def create_evolved(self) -> CreatureOne:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactoryOne):
    def create_base(self) -> CreatureOne:
        return Shiftling()

    def create_evolved(self) -> CreatureOne:
        return Morphagon()
