import sys


def main() -> None:
    print("=== Command Quest ===")
    argv = sys.argv
    argc = len(argv)
    i = 0
    first = 1
    while i < argc:
        if i == 0:
            print(f"Program name: {argv[i]}")
        else:
            print(f"Argument {i}: {argv[i]}")
        if argc == 1:
            print("No arguments provided!")
        elif argc != 1 and first == 1:
            print(f"Arguments received: {argc-1}")
            first = 0
        i = i + 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
