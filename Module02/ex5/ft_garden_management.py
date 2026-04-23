class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} sucessfully")

    def water_plants(self) -> None:
        print("\nWatering plants...")
        print("Opening watering system")

        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too high (max 12)")
        print(f"{plant_name}: healthy (water: {water_level},"
              f"sun: {sunlight_hours})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    garden.water_plants()

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        garden.check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
