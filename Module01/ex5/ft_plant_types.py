class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade_area: float = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} "
              f"square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    print(f"\n{oak.name} (Tree): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
