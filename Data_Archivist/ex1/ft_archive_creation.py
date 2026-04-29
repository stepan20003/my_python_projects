import sys
import typing


def transform(text: str) -> str:
    result = text.replace("\n", "#\n")
    return result


def display(file: typing.IO) -> str:
    print("---")
    text = file.read()
    print(text)
    print("---")
    return transform(text)


def main() -> None:
    argv = sys.argv
    if len(argv) == 2:
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file {argv[1]}")
            fd = open(argv[1])
            text = display(fd)
            fd.close()
            print(f"File {argv[1]} closed.")
            print("Transform data:")
            print(f"---\n{text}\n---")
            new_file = input("Enter new file name (or empty):")
            try:
                fd = open(new_file, "w")
                print(f"Saving data to {new_file}")
                fd.write(text)
                fd.close()
                print(f"Data saved in file '{new_file}'.")
            except Exception:
                print("Not saving data.")
        except Exception as e:
            print(f"Error opening file {argv[1]}: {e}")
    else:
        print("Usage: ft_ancient_text.py <file>\n")


if __name__ == "__main__":
    main()
