def secure_archive(file: str, text: str,
                   content: str = None) -> tuple[bool, str]:
    if text == "r":
        try:
            with open(file, "r") as fd:
                print("Using 'secure_archive' to read from a regular file:")
                tuple1 = (True, fd.read())
        except FileNotFoundError as e:
            print("Using 'secure_archive' to read from a nonexistent file:")
            tuple1 = (False, str(e))
        except PermissionError as e:
            print("Using 'secure_archive' to read from an inaccessible file:")
            tuple1 = (False, str(e))
    elif text == "w":
        try:
            with open(file, "w") as fd:
                fd.write(content)
                print("Using 'secure_archive' to write "
                      "previous content to a new file:")
                tuple1 = (True, 'Content successfully written to file')
        except PermissionError as e:
            print("Using 'secure_archive' to write to an inaccessible file:")
            tuple1 = (False, str(e))
        except Exception as e:
            tuple1 = (False, str(e))
    return tuple1


if __name__ == "__main__":
    print(secure_archive('/not/existing/file', 'r'))
    print(secure_archive('/etc/master.passwd', 'r'))
    print(secure_archive('ancient_fragment.txt', 'r'))
    print(secure_archive('ancient_fragment.txt',
                         'w', "i am best programerrrrr"))
