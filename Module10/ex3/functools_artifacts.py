import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
            'add': operator.add,
            'multiply': operator.mul,
            'max': lambda a, b: a if a > b else b,
            'min': lambda a, b: a if a < b else b,
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
            'fire_enchant': functools.partial(base_enchantment, power=50,
                                              element='fire'),
            'ice_enchant': functools.partial(base_enchantment, power=50,
                                             element='ice'),
            'lightning_enchant': functools.partial(base_enchantment, power=50,
                                                   element='lightning'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatch(value: Any) -> str:
        return f"Unknown spell type: {type(value)}"

    @dispatch.register(int)
    def _(value: int) -> str:
        return f"Damage spell dealing {value} damage"

    @dispatch.register(str)
    def _(value: str) -> str:
        return f"Enchantment spell: {value}"

    @dispatch.register(list)
    def _(value: list) -> str:
        return f"Multi-cast spell hitting {len(value)} targets"

    return dispatch


def main() -> None:
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonnaci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting partial enchanter...")

    def base_enchant(item: str, power: int, element: str) -> str:
        return f"{element} enchant on {item} with {power} power"

    enchanter = partial_enchanter(base_enchant)
    print(enchanter['fire_enchant']("Sword"))
    print(enchanter['ice_enchant']("Shield"))
    print(enchanter['lightning_enchant']("Axe"))

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(100))
    print(dispatch("Flame"))
    print(dispatch([1, 2, 3]))
    print(dispatch({"key": 1}))


if __name__ == "__main__":
    main()
