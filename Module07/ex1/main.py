from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Common", 3,
                               "+1 mana per turn"))
    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    while True:
        try:
            card = deck.draw_card()
            info = card.get_card_info()
            print(f"Drew: {card.name} ({info.get('type', 'Unknown')})")
            print(f"Play result: {card.play({})}\n")
        except IndexError:
            break

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
