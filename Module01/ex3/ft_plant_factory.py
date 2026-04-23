class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    count = 0
    print("=== Plant Factory Output ===")
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        print(f"Created: {name} ({height}cm, {age} days)")
        count += 1
    print(f"\nTotal plants created: {count}")
