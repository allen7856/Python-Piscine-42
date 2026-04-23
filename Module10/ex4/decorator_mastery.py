import time
import functools
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> object:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> object:
            power = kwargs.get('power')
            if power is None:
                if args and hasattr(args[0], '__dict__'):
                    power = args[2] if len(args) > 2 else 0
                else:
                    power = args[0] if args else 0
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"({attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))

    print("\nTesting power validation...")
    print(guild.cast_spell(power=15, spell_name="Lightning"))
    print(guild.cast_spell(power=5, spell_name="Lightning"))

    print("\nTesting retry_spell decorator...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        unstable_spell.attempts += 1
        if unstable_spell.attempts < 3:
            raise RuntimeError("Magic fizzled")
        return "Spell finally succeeded!"

    unstable_spell.attempts = 0
    print(unstable_spell())


if __name__ == "__main__":
    main()
