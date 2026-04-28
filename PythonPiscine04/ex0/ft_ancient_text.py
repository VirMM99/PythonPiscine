from typing import TextIO
import sys


def main() -> None:
    # If they dont give you the file in the arguments(argv[1] is missing)
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f: TextIO = open(filename, "r")
    except Exception as e:
        print(f"Error opnening file '{filename}': {e}")
        return
    print("---")
    print()
    print(f.read())
    print()
    print("\n---")

    f.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
