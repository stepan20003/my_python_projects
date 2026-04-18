def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return 0


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("Input data is '25'")
    x = input_temperature('25')
    print(f"Temperature is now {x}°C")
    print("Input data is 'abc'")
    x = input_temperature("abc")

    print("All tests completed - program didn't crash!")


test_temperature()
