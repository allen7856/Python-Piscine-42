from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"After +10: {acc(10)}")
    print(f"After +20: {acc(20)}")
    print(f"After -30: {acc(-30)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault['store']
    recall = vault['recall']
    store("spell", "Fireball")
    store("power", 9000)
    print(recall("spell"))
    print(recall("power"))
    print(recall("unknown"))


if __name__ == "__main__":
    main()
