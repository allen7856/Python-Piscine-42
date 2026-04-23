from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches: list[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.split()[0].lower()}_001"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating,
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda item: item[1].rating,
            reverse=True,
        )
        return [
            {
                'rank': i + 1,
                'id': card_id,
                'name': card.name,
                'rating': card.rating,
                'record': f"{card.wins}-{card.losses}",
            }
            for i, (card_id, card) in enumerate(sorted_cards)
        ]

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        avg_rating = (
            sum(c.rating for c in self._cards.values()) // total
            if total else 0
        )
        return {
            'total_cards': total,
            'matches_played': len(self._matches),
            'avg_rating': avg_rating,
            'platform_status': 'active',
        }
