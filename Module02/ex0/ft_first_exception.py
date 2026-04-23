def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        return temp
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"'{temp_str}' is not a valid number")
        else:
            raise


def test_temperature_input() -> None:
    test_values: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for value in test_values:
        print(f"Testing temperature: {value}")
        try:
            temp = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants!\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
