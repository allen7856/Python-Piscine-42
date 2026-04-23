import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


CREATURES = {
        'dragon': ('Fire Dragon', 5, 'Legendary', 7, 5),
        'goblin': ('Goblin Warrior', 2, 'Common', 3, 2),
        }

SPELLS = {
        'fireball': ('Lightning Bolt', 3, 'Rare', 'damage'),
        }

ARTIFACTS = {
        'mana_ring': ('Mana Crystal', 2, 'Common', 3, '+1 mana per turn'),
        }


class FantasyCardFactory(CardFactory):
    def get_supported_types(self) -> dict:
        return {
                'creatures': list(CREATURES.keys()),
                'spells': list(SPELLS.keys()),
                'artifacts': list(ARTIFACTS.keys()),
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in CREATURES else 'dragon'
        args = CREATURES[key]
        return CreatureCard(*args)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in SPELLS else 'fireball'
        args = SPELLS[key]
        return SpellCard(*args)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in ARTIFACTS else 'mana_ring'
        args = ARTIFACTS[key]
        return ArtifactCard(*args)

    def create_themed_deck(self, size: int) -> dict:
        creators = [self.create_creature, self.create_spell,
                    self.create_artifact]
        cards = [random.choice(creators)() for _ in range(size)]
        return {
                'deck': cards,
                'size': size,
                'theme': 'Fantasy',
        }
