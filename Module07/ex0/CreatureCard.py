from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive number.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Heath must be a positive number")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield',
        }

    def attack_target(self, target: 'Card') -> dict:
        return {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': True
                }
