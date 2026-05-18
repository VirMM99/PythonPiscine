from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any

# Todas las func de este dicc:
# Reciben dos ints
# Devuelven un int
operations: dict[str, Callable[[int, int], int]] = {
    "add": add,
    "multiply": mul,
    "max": max,
    "min": min
}


# Recibe una lista de nums, el nombre de una operación
# y devuelve un número
def spell_reducer(spells: list[int], operation: str) -> int:
    # 1era Validation:Si la lista está vacía, Cero al canto
    if not spells:
        return 0
    # 2Valid:si la operation no existe, lanza error
    if operation not in operations:
        raise ValueError("Unknown operation")
    # Y aquí la canción de 'Oh oh oh it's magic'
    # Porque con reduce ocurre la *Magia*
    return reduce(operations[operation], spells)


# Recibe una func.
def partial_enchanter(
        base_enchantment: Callable
        ) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }


# el caché significa "guarda los resultados anteriores"
# ex:fib(10) lo calcula UNA vez
# y la siguiente llamada es instantanea
# maxsize es cuantos resultados quieres guardar
# y con None es que NO ponemos límite(Guarda Todo)
@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


# Esto ya es Magia negra. Significa que esta func cambiará
# según el tipo
def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    # spell mira el tipo y decide que versión usar
    def spell(value: Any) -> str:
        return "Unknown spell type"

    # Voy a registrar una nueva versión de spell
    @spell.register
    # _ Porque el nombre no importa,
    # el dispatcher USA el TIPO anotado
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"
    return spell


if __name__ == "__main__":

    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")

    def enchantment(
            power: int,
            element: str,
            target: str
    ) -> str:
        return (
            f"{element} attack with "
            f"{power} power on {target}"
        )
    enchantments = partial_enchanter(enchantment)
    print(enchantments["fire"]("dragon"))
    print(enchantments["ice"]("goblin"))
    print(enchantments["lightning"]("wizard"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nCache info:")
    # muestra hits, misses y tamaño caché
    # Hits:veces que encontró el resultado
    # Misses:veces que tuvo que calcular
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
