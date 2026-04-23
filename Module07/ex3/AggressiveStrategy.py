from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
                available_targets,
                key=lambda t: t.get('health', 0)
        )

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = []
        mana_used = 0
        damage_dealt = 0
        available_mana = 10

        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if card.is_playable(available_mana - mana_used):
                played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.cost

        targets = self.prioritize_targets([{'name': 'Enemy Player',
                                            'health': 20}])
        target_names = [t['name'] for t in targets]

        return {
                'strategy': self.get_strategy_name(),
                'actions': {
                    'cards_played': played,
                    'mana_used': mana_used,
                    'targets_attacked': target_names,
                    'damage_dealt': damage_dealt,
                }
        }
