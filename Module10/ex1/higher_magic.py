from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwargs) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    def damage(power: int) -> int:
        return power

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {mega(10)}")

    print("\nTesting conditional caster...")

    def is_strong(power: int) -> bool:
        return power > 50

    def lightning(power: int) -> str:
        return f"Lightning strikes with {power} power"

    conditional = conditional_caster(is_strong, lightning)
    print(conditional(60))
    print(conditional(30))

    print("\nTesting spell sequence...")

    def ice(target: str) -> str:
        return f"Ice hits {target}"

    def wind(target: str) -> str:
        return f"Wind blows {target}"

    sequence = spell_sequence([fireball, ice, wind])
    results = sequence("Goblin")
    print("Sequence results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
