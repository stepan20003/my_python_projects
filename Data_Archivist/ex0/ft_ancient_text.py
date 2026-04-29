import sys
import typing


def display(file: typing.IO) -> None:
    print("---")
    print(file.read())
    print("---")


def main() -> None:
    argv = sys.argv
    if len(argv) == 2:
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{argv[1]}'")
            fd = open(argv[1])
            display(fd)
            fd.close()
            print(f"File '{argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{argv[1]}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>\n")


if __name__ == "__main__":
    main()
