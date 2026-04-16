def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===")
    try:
        x = input_temperature('25')
        print(f"Temperature is now {x}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        x = input_temperature('abc')
        print(f"Temperature is now {x}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
