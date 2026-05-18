import time
from collections.abc import Callable
from functools import wraps


# Recibe una función
def spell_timer(func: Callable) -> Callable:
    # Mantén el nombre y metadata original
    @wraps(func)
    # Esto para aceptar cualquier argumento
    # args:captura arg normales
    # kwargs:captura argumentos con nombre
    def wrapper(*args, **kwargs):
        # __name__ para que se vea el
        # nombre de la func como texto
        print(f"Casting {func.__name__}...")
        # módulo.función() de Time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # .3f es para que saque 3 decimales
        print(
            f"Spell completed in "
            f"{end - start:.3f} seconds"
        )
        return result
    return wrapper


# Aquí usaremos decorador CON parámetros
# primero recibe el parámetro y luego la func
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # -1 porque es el último elemento
            power = args[-1]
            # si tienes power suficiente
            # puedes lanzar el hechizo
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


# Esto es por si falla que lo vuelva a intentar
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    # -1 para en los 2 primeros intentos retry
                    # y en el 3 ya de el mensaje
                    if attempt < max_attempts - 1:
                        # ponemos attempt +1 porque
                        # los attempts empiezan en 0,1,2..
                        # y queremos que imprima desde
                        # "intento 1, 2, 3..."
                        print(
                            "Spell failed, retrying..."
                            f" ({attempt + 1}/{max_attempts})"
                        )
            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    # Ésta no necesita self, atributos ni instancia
    # solo verifica un str
    # Valida min 3 chars y solo letras y spaces
    def validate_mage_name(name: str) -> bool:
        # elimina spaces y comprueba letras
        return (
            len(name) >= 3
            and name.replace(" ", "").isalpha()
        )
    # Recibe el objeto self = args[0]
    # spell_name = args[1]
    # power = args[2]

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:
        return (
            "Successfully cast "
            f"{spell_name} with {power} power"
        )


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        # sleep para simular tiempo real
        time.sleep(0.1)
        return "Fireball cast!"
    print("Result:", fireball())

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def failed_spell() -> str:
        raise Exception("Spell failed")
    print(failed_spell())

    print("\nTesting MageGuild...")
    print(
        MageGuild.validate_mage_name("Gandalf")
    )
    print(
        MageGuild.validate_mage_name("R2")
    )

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
