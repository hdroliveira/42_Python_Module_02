class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def simulate_garden_error(error_type: str) -> None:
    if error_type == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif error_type == "water":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        simulate_garden_error("plant")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        simulate_garden_error("water")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        simulate_garden_error("plant")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        simulate_garden_error("water")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
