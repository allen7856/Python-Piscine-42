from ex2.EliteCard import EliteCard, CombatType, SpellType


def main() -> None:
    print("=== DataDeck Ability System ===")

    warrior = EliteCard(
            "Arcane Warrior", 6, "Legendary",
            attack_power=5, defense=3, mana=8,
            combat_type=CombatType.MELEE,
            spell_type=SpellType.FIRE,
    )

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("\nCombat phase:")

    class DummyTarget:
        name = "Enemy"

    print(f"Attack result: {warrior.attack(DummyTarget())}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")

    class DummyTarget2:
        name = "Enemy1"

    class DummyTarget3:
        name = "Enemy2"

    print(f"Spell cast: {warrior.cast_spell('Fireball',
          [DummyTarget2(), DummyTarget3()])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
