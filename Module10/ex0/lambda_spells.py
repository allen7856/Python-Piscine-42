def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    # sort artifacts by their 'power' value from highest to lowest
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    # return only mages whose 'power' is greater than or equal to min_power
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    # transform each spell by wrapping it in "* ... *"
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    # extract mage powers and compute max, min and average power
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(
            sum(map(lambda m: m['power'], mages)) / len(mages), 2
        ),
    }


def main() -> None:
    artifacts = [
            {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
            {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
            {'name': 'Shadow Cloak', 'power': 78, 'type': 'armor'},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
            f"{sorted_artifacts[0]['name']}"
            f" ({sorted_artifacts[0]['power']} power)"
            f" comes before "
            f"{sorted_artifacts[1]['name']}"
            f" ({sorted_artifacts[1]['power']} power)"
    )

    spells = ['fireball', 'heal', 'shield']
    print("\nTesting spell transformer...")
    print(' '.join(spell_transformer(spells)))

    mages = [
            {'name': 'Aldor', 'power': 30},
            {'name': 'Belwyn', 'power': 80},
            {'name': 'Cyra', 'power': 55},
    ]
    print("\nTesting power filter...")
    filtered = power_filter(mages, 50)
    print("Mages with power >= 50:")
    for m in filtered:
        print(f"{m['name']} ({m['power']} power)")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
