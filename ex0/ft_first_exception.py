def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)

        if temp > 40:
            print(f"Error {temp}°C is too hot for plants (max 40°C)\n")
            return None
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    test1 = "25"
    print(f"\nTesting temperature: {test1}")
    check_temperature(test1)

    test2 = "abc"
    print(f"Testing temperature: {test2}")
    check_temperature(test2)

    test3 = "100"
    print(f"\nTesting temperature: {test3}")
    check_temperature(test3)

    test4 = "-50"
    print(f"Testing temperature: {test4}")
    check_temperature(test4)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
