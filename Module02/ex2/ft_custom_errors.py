class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_catch_all_garden_errors() -> None:
    print("\nTesting catching all garden errors...")

    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_catch_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
