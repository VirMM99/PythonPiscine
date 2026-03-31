

def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp_str}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    value = input_temperature("25")
    print(f"Temperature is now: {value}°C")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("100")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("-50")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash")


test_temperature()

# try:
#     num = int("abc")
# except ValueError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
