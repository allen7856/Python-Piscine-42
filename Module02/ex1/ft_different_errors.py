def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        result: int = int("abc")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        result_div: float = 10 / 0
        print(f"Result: {result_div}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        content: str = f.read()
        f.close()
        print(f"Result: {content}")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden: dict[str, str] = {"tomato": "red"}
        color: str = garden["missing_plant"]
        print(f"Result: {garden}, {color}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        num: int = int("0")
        division: float = 100 / num
        print(f"Result: {num}, {division}")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
