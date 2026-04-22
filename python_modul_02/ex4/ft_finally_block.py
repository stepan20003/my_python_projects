
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        GardenError.__init__(self, message)


def water_plant(plant_name: str) -> None:
    if (plant_name == str.capitalize(plant_name)):
        print(f"Watering {plant_name}:[OK]")
    else:
        raise PlantError("Invalid plant name to water")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    print("Opening watering system")
    x = ["Tomato", "Lettuce", "Carrots"]
    try:
        for i in x:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}: {i}", end='\n')
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\n")
    print("Testing valid plants...")
    print("Opening watering system")
    x[1] = "lettuce"
    try:
        for i in x:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}: {i}", end="\n")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
