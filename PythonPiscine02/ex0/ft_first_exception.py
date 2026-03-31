

def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    value = input_temperature("25")
    print(f"Temperature is now: {value}°C")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash")


test_temperature()
