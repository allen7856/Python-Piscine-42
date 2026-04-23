from enum import Enum
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"


class SpellType(Enum):
    FIRE = "fire"
    ICE = "ice"
    LIGHTNING = "lightning"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense: int, mana: int,
                 combat_type: CombatType = CombatType.MELEE,
                 spell_type: SpellType = SpellType.FIRE) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana
        self.combat_type = combat_type
        self.spell_type = spell_type

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Elite'
        info['attack_power'] = self.attack_power
        info['defense'] = self.defense
        info['mana'] = self.mana
        return info

    def play(self, game_state: dict) -> dict:
        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Elite card enters '
                'battlefield with combat and magic abilities'
        }

    def attack(self, target: 'Card') -> dict:
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
                'attacker': self.name,
                'target': target_name,
                'damage': self.attack_power,
                'combat_type': self.combat_type.value,
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
                'defender': self.name,
                'damage_taken': taken,
                'damage_blocked': blocked,
                'still_alive': True
                }

    def get_combat_stats(self) -> dict:
        return {
                'attack_power': self.attack_power,
                'defense': self.defense,
                'combat_type': self.combat_type.value
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = len(targets) + 2
        self.mana -= mana_used
        target_names = [t.name if hasattr(t, 'name') else str(t)
                        for t in targets]
        return {
                'caster': self.name,
                'spell': spell_name,
                'targets': target_names,
                'mana_used': mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
                'channeled': amount,
                'total_mana': self.mana,
        }

    def get_magic_stats(self) -> dict:
        return {
                'mana': self.mana,
                'spell_type': self.spell_type.value,
        }
