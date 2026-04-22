import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        x: list[str] = ["", "", ""]
        j = 0
        s = input("Enter new coordinates as floats in format 'x,y,z':")
        try:
            for i in s:
                if i == ",":
                    j += 1
                    continue
                else:
                    x[j] += i
                    continue
            if j != 2:
                raise SyntaxError
            return (float(x[0]), float(x[1]), float(x[2]))
        except ValueError as e:
            print(f"Error on parameter {x[j]}: {e}")
        except Exception:
            print("Invalid syntax")


def get_distance() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    x, y, z = get_player_pos()
    tuple1 = x, y, z
    print(f"Got a first tuple: {tuple1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0
    dist = round(math.sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2), 4)
    print(f"Distance to center: {dist}\n")
    print("Get a second set of coordinates")
    x1, y1, z1 = get_player_pos()
    dist = round(math.sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist}")


if __name__ == "__main__":
    get_distance()
