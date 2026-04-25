def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    numb = int(temp_str)
    if numb >= 0 and numb <= 40:
        return numb
    elif numb > 40:
        raise ValueError(f"{numb}°C is too hot for plants (max 40°C)")
    elif numb < 0:
        raise ValueError(f"{numb}°C is too cold for plants (min 0°C)")
    else:
        return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for i in ['25', 'abc', '100', '-50']:
        try:
            z = input_temperature(i)
            print(f"Temperature is now {z}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    test_temperature()
