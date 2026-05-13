# key:value, usamos Key para usar el value de power para ordenar
# Por defecto suele sorted de menor a mayor, Usamos reverse=True
# para que vaya de mayor a menor
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


# Queremos una lista que filtre a los magos por su valor min
# Devuelve list porque el ejercicio quiere una lista
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


# Transforma nombres de hechizos y le queremos añadir texto
def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


# Calcula max porder, min poder y promedio
def mage_stats(mages: list[dict]) -> dict:
    #  le ponemos al final ["power"] para que nos devuelva el numero
    # solo, sin eso nos devolvería todo el mago con mas power(=min)
    max_power = max(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    min_power = min(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    # le hacemos round(...,2) para que nos de con dos decimales
    average_power = round(
        sum(mage["power"] for mage in mages) / len(mages),
        2
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "average_power": average_power
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {
            "name": "Crystal Orb",
            "power": 85,
            "type": "magic"
        },
        {
            "name": "Fire Staff",
            "power": 92,
            "type": "fire"
        }
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]["name"]} "
        f"({sorted_artifacts[0]["power"]} power)"
        f" comes before "
        f"{sorted_artifacts[1]["name"]} "
        f"({sorted_artifacts[1]["power"]} power)"
    )
    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
