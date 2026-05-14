from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


# mega_fireball = power_amplifier(fireball, 3)
# Recibe dos funciones (spells)
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    # Dentro creamos una nueva función. Devuelve Tupla
    return lambda target, power: (
        spell1(target, power),
        spell2(target, power)
    )


# Recibes spell + multiplier. Crear una spell mas fuerte
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    # Creas una nueva función. Multiplicas el poder
    return lambda target, power: (
        base_spell(target, power * multiplier)
    )


# Lanzar spell ONLY if the condition is TRUE
# Recibe condition + spell
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    # Nueva función
    return lambda target, power: (
        spell(target, power)
        # Revisamos condición. Si true:
        if condition(target, power)
        # Si false:
        else "Spell fizzled"
    )


# Se usa esta funcion en conditional caster y se pone target
# porque en el subject dice que tanto condition como spell
#  reciven los mismo argumentos
def enough_power(target: str, power: int) -> bool:
    return power >= 20


# Ejecutar Muchas spells una detrás de otra. Recibe una lista.
def spell_sequence(spells: list[Callable]) -> Callable:
    # Nueva función crear lista de resultados y recorrer spells
    return lambda target, power: [
        spell(target, power)
        for spell in spells
    ]


if __name__ == "__main__":

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    result1, result2 = combo("Dragon", 10)
    print(f"Combined spell result: {result1} | {result2}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    original_power = 10
    amplified_power = original_power * 3
    print(
        f"Original: {original_power}, "
        f"Amplified: {amplified_power}"
    )

    print("\nTesting conditional caster...")
    conditional = conditional_caster(enough_power, fireball)
    print(conditional("Dragon", 5))
    print(conditional("Dragon", 30))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for result in sequence("Dragon", 10):
        print(result)
