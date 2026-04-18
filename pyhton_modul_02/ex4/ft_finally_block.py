class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        GardenError.__init__(self, message)

def water_plant(plant_name: str):
    try:
        if(plant_name == str.capitalize(plant_name)):
            print(f"Watering {plant_name}:[OK]")
        else:
            raise PlantError("Invalid plant name to water")
    except PlantError as e:
        print(f"{e}")

def test_watering_system():
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    print("Opening watering system")
    x = ["Tomato","lettuce","Carrots"]
    for i in x:
        try:
            water_plant(i)
        except PlantError as e:
            str.capitalize(i)
        finally:
            water_plant(i)



if __name__ == "__main__":
    test_watering_system()

