from collections.abc import Callable

# Funciones que recuerdan variables(eso es un closure)
# Función que devuelve otra función
# cuenta llamadas y recuerda el valor
def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        # porque queremos modificar count
        nonlocal count
        count += 1
        return count
    return counter


# Acumula poder
def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


# Crear funciones personalizadas
def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    # Crear memoria Privada
    memory = {}
    # Guarda cosas
    def store(key: str, value: object) -> None:
        memory[key] = value
    # Busca cosas
    def recall(key: str) -> object:
        # Si existe
        if key in memory:
            return memory[key]
        # Si no existe
        return "Memory not found"
    return {
        "store": store,
        "recall": recall
        }


if __name__ == "__main__":

    print("Testing mage counter...")
    counter_a = mage_counter()
    print(counter_a())
    print(counter_a())
    # Cada clousure tiene su propia memoria
    # empieza desde 0 otra vez
    counter_b = mage_counter()
    print(counter_a())

    print("\nTesting spell acumulator...")
    power = spell_accumulator(100)
    print(power(20))
    print(power(30))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))
