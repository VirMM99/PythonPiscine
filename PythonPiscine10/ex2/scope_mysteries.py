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
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    # Cada clousure tiene su propia memoria
    # empieza desde 0 otra vez
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell acumulator...")
    power = spell_accumulator(100)
    print(f"Base 100, add 20: {power(20)}")
    print(f"Base 100, add 30: {power(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
