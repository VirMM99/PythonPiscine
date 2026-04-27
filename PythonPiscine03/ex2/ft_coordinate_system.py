

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
                            "Enter new coordinates as "
                            "floats in format 'x,y,z': ")
        parts = user_input.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        valid_coord = []
        error = False
        for arg in parts:
            try:
                valid_coord.append(float(arg.strip()))
            except ValueError:
                print(
                    f"Error on parameter '{arg.strip()}': "
                    f"could not convert string to float: '{arg.strip()}'")
                error = True
                break
        if not error:
            return (valid_coord[0], valid_coord[1], valid_coord[2])


def calculate_distance(position: tuple[float, float, float]) -> float:
    x, y, z = position
    return math.sqrt(x**2 + y**2 + z**2)


def distance_in_between(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {round(calculate_distance(pos1), 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_in_between(pos1, pos2), 4)}")
