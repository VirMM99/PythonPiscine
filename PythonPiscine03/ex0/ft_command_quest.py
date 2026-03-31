import sys

def count_of_args(av: str) -> None:
    print(f"Program name: {av[0]}")
    if len(av) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(av) - 1}")
        for num in range(1, len(av)):
            print(f"Argument {num}: {av[num]}")
    print(f"Total arguments: {len(av)}")

if __name__ == "__main__":
    print("=== Command Quest ===")
    count_of_args(sys.argv)