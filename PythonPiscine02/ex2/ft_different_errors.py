

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("open_me_this.txt")
    elif operation_number == 3:
        "Hilda" + 3
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for num in range(0, 5):
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
        except ValueError as e:
            print(f"Caught garden_operations error: {e}")
        except ZeroDivisionError as e:
            print(f"Caught garden_operations error: {e}")
        except FileNotFoundError as e:
            print(f"Caught garden_operations error: {e}")
        except TypeError as e:
            print(f"Caught garden_operations error: {e}")
    print("\nAll tests completed - program didn't crash")


test_error_types()
