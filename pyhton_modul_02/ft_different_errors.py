def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 12
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    x = [0, 1, 2, 3, 4]
    for i in x:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except Exception as e:
            print(f"Caught {type(e).__name__}:{e}")


if __name__ == "__main__":
    test_error_types()
