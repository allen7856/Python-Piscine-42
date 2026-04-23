from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 6, 1150)

    platform = TournamentPlatform()
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        print(f"{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print(f"\nPlatform Report:\n{platform.generate_tournament_report()}")
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
