from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense: int, base_rating: int = 1000) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Tournament'
        info['attack_power'] = self.attack_power
        info['defense'] = self.defense
        return info

    def play(self, game_state: dict) -> dict:
        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Tournament card enters the arena',
        }

    def attack(self, target: 'TournamentCard') -> dict:
        return {
                'attacker': self.name,
                'target': target.name,
                'damage': self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
                'defender': self.name,
                'damage_taken': taken,
                'damage_blocked': blocked,
        }

    def get_combat_stats(self) -> dict:
        return {
                'attack_power': self.attack_power,
                'defense': self.defense,
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
                'name': self.name,
                'rating': self.rating,
                'wins': self.wins,
                'losses': self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
                'name': self.name,
                'rating': self.rating,
                'record': f"{self.wins}-{self.losses}",
                'attack_power': self.attack_power,
                'defense': self.defense,
        }
