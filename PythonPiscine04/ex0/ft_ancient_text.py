

import sys


def main():
    # If they dont give you the file in the arguments(argv[1] is missing)
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
    except Exception as e:
        print(f"Error opnening file '{filename}': {e}")
        return
    print("---", end="")
    for line in f:
        print(line, end="")
    print()
    print("\n---")

    f.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()

# ❓ Important question from exercise:
# What is the type of the data returned by open()?
# 👉 Answer: a file object (a stream you can read)
# <class '_io.TextIOWrapper'>  type of typing.IO
