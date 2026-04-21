

import sys


def main():
    # If they dont give you the file in the arguments(argv[1] is missing)
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    content = []
    print("---\n")
    for line in f:
        content.append(line)
        print(line, end="")
    print("\n")
    print("---")

    f.close()
    print(f"File '{filename}'closed.")
    new_content = []
    print()
    print("Transform data:")
    print("---\n")
    for line in content:
        line = line.rstrip("\n") + "#"
        new_content.append(line)
        print(line)
    print("\n")
    print("---")

    new_file = input("Enter new file name (or empty):")
    if new_file == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file}'")
    f = open(new_file, "w")
    for line in new_content:
        f.write(line + "\n")
    f.close()
    print(f"Data saved in file '{new_file}'")


if __name__ == "__main__":
    main()

# Structure you should have now
# 1.Read file + store content
# 2.Print original
# 3.Close file
# 4.Transform content
# 5.Print transformed
# 6.Ask user input
# Save or not
