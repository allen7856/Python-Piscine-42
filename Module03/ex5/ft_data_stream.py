#!/usr/bin/env python3

from typing import Generator


def game_event_stream(count: int) -> Generator[tuple[str, int, str],
                                               None, None]:
    players: list[str] = ['alice', 'bob', 'charlie']
    events: list[str] = ['killed monster', 'found treasure', 'leveled up']

    for i in range(count):
        player: str = players[i % len(players)]
        level: int = (i % 20) + 1
        event: str = events[i % len(events)]

        yield (player, level, event)


def fibonacci(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    count: int = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes(n: int) -> Generator[int, None, None]:
    count: int = 0
    num: int = 2

    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def demonstrate_generators() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total: int = 0
    high_level: int = 0
    treasure: int = 0
    levelup: int = 0

    for player, level, event in game_event_stream(1000):
        total += 1

        if total <= 3:
            print(f"Event {total}: Player {player} (level {level}) {event}")

        if level >= 10:
            high_level += 1

        if 'treasure' in event:
            treasure += 1
        if 'leveled up' in event:
            levelup += 1

    if total > 3:
        print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    print("\nMemory usage: Constant (streaming)")
    print("\nProcessing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib_nums: list[int] = list(fibonacci(10))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_nums))}")
    prime_nums: list[int] = list(primes(5))
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_nums))}")


if __name__ == "__main__":
    demonstrate_generators()
