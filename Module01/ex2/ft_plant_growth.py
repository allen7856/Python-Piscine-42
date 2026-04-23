class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1

    def age_plant(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    start_height: int = rose.height
    for day in range(6):
        rose.grow()
        rose.age_plant()
    print("=== Day 7 ===")
    print(rose.get_info())
    growth: int = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
