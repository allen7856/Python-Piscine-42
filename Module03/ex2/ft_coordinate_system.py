import math
import sys


def parse_coordinates(coord_string: str) -> tuple[int, int, int] | None:
    try:
        parts = coord_string.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None
    except TypeError:
        print('Try again! The program needs 3 numbers in the "x,y,z" format')
        return None


def calculate_distance(point1: tuple[int, int, int],
                       point2: tuple[int, int, int]) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def demonstrate_coordinates() -> None:
    print("=== Game Coordinate System ===")

    count: int = 0
    for arg in sys.argv:
        count += 1

    if count == 1:
        position = (10, 20, 5)
        print(f"\nPosition created: {position}")

        origin = (0, 0, 0)
        dist = calculate_distance(origin, position)
        print(f"Distance between {origin} and {position}: {dist:.2f}")

        print('\nParsing coordinates: "3,4,0"')
        parsed = parse_coordinates("3,4,0")
        if parsed:
            print(f"Parsed position: {parsed}")
            dist2 = calculate_distance(origin, parsed)
            print(f"Distance between {origin} and {parsed}: {dist2:.1f}")

        print('\nParsing invalid coordinates: "abc,def,ghi"')
        parse_coordinates("abc,def,ghi")

        if parsed:
            print("\nUnpacking demonstration:")
            x, y, z = parsed
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")

    elif count == 2:
        position_from_arg = parse_coordinates(sys.argv[1])
        if position_from_arg:
            print(f"Position created: {position_from_arg}")
            origin = (0, 0, 0)
            dist3 = calculate_distance(origin, position_from_arg)
            print(f"Distance between {origin} and "
                  f"{position_from_arg}: {dist3:.2f}")
            print("\nUnpacking demonstration:")
            x, y, z = position_from_arg
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
        else:
            print("Invalid coordinates provided.")

    else:
        print('Invalid arguments - the program needs 3 numbers in the "x,y,z"'
              'format.')


if __name__ == "__main__":
    demonstrate_coordinates()
