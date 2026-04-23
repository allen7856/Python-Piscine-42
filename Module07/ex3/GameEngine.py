from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0
        self._hand: list = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        dragon = factory.create_creature('dragon')
        goblin = factory.create_creature('goblin')
        bolt = factory.create_spell('fireball')
        self._hand = [dragon, goblin, bolt]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        hand_display = [
                f"{c.name} ({c.cost})" for c in self._hand
        ]
        result = self._strategy.execute_turn(self._hand, [])
        self._turns += 1
        self._total_damage += result['actions']['damage_dealt']
        return {
                'hand': hand_display,
                'turn_execution': result,
        }

    def get_engine_status(self) -> dict:
        return {
                'turns_simulated': self._turns,
                'strategy_used': (
                    self._strategy.get_strategy_name()
                    if self._strategy else None
                ),
                'total_damage': self._total_damage,
                'cards_created': self._cards_created,
        }
