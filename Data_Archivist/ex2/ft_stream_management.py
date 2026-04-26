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


def main():
    argv = sys.argv
    if len(argv) == 2:
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{argv[1]}'")
            fd = open(argv[1])
            text = display(fd)
            fd.close()
            print(f"File '{argv[1]}' closed.")
            print("Transform data:")
            print(f"---\n{text}\n---")
            print("Enter new file name (or empty):", end=" ", flush=True)
            new_file = sys.stdin.readline()[:-1]
            try:
                fd = open(new_file, "w")
                print(f"Saving data to '{new_file}'")
                fd.write(text)
                fd.close()
                print(f"Data saved in file '{new_file}'.")
            except PermissionError as e:
                print(f"[STDERR] Error opening file"
                      f" '{new_file}' {e}", file=sys.stderr)
                print("Data not saved.", file=sys.stderr)
            except Exception:
                print("Not saving data.", file=sys.stderr)
        except Exception as e:
            print(f"[STDERR] Error opening file"
                  f" '{argv[1]}': {e}", file=sys.stderr)
    else:
        print("Usage: ft_ancient_text.py <file>\n")


if __name__ == "__main__":
    main()
