from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    turn = engine.simulate_turn()

    print(f"Hand: {turn['hand']}")
    print("Turn execution:")
    execution = turn['turn_execution']
    print(f"Strategy: {execution['strategy']}")
    print(f"Actions: {execution['actions']}\n")

    print(f"Game Report:\n{engine.get_engine_status()}")
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
