class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color: str = flower_color
        self.blooming: bool = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points: int = prize_points


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added: int = 0
            self.total_growth: int = 0

        def record_growth(self) -> None:
            self.total_growth += 1

        def record_plant_added(self) -> None:
            self.plants_added += 1

    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.record_plant_added()
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all_plants(self) -> None:
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def get_score(self) -> int:
        score: int = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    def print_report(self) -> None:
        print(f"\n==={self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        regular_count: int = 0
        flowering_count: int = 0
        prize_count: int = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.flower_color} flowers (blooming), "
                      f"Prize points: {plant.prize_points}")
                prize_count += 1
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.flower_color} flowers (blooming)")
                flowering_count += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                regular_count += 1
        print(f"Plants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {regular_count} regular, "
              f"{flowering_count} flowering, "
              f"{prize_count} prize flowers")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['GardenManager']:
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @classmethod
    def get_total_gardens(cls) -> int:
        return cls.total_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.grow_all_plants()
    alice_garden.print_report()
    print(f"\nHeight validation test: "
          f"{GardenManager.validate_height(100)}")
    bob_garden = GardenManager("Bob")
    bob_score: int = 92
    print(f"Garden scores - Alice {alice_garden.get_score()}, "
          f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
