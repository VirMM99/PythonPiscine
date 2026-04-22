

from elements import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion():
    return (
            "Healing potion brewed with"
            f" '{create_earth()}' and '{create_air()}'"
        )


def strength_potion():
    return (
            "Strength potion brewed with"
            f" '{create_fire()}' and '{create_water()}'"
        )
