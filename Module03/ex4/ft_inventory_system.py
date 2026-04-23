#!/usr/bin/env python3

import sys


def inventory_system() -> None:
    if len(sys.argv) == 1:
        print("No info! The program needs at least "
              "one argument writen as 'item:quantity'")
        return

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            parts: list[str] = arg.split(":")
            if len(parts) != 2:
                raise ValueError
            item: str = parts[0]
            quantity: int = int(parts[1])
            inventory[item] = inventory.get(item, 0) + quantity
        except ValueError:
            print("Invalid info! The program needs at least "
                  "one argument writen as 'item:quantity'")
            return

    total: int = sum(inventory.values())
    unique: int = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique}")

    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        percentage: float = (quantity / total) * 100
        unit_text = "unit" if quantity == 1 else "units"
        print(f"{item}: {quantity} {unit_text} "
              f"({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most_item: str = ""
    most_qty: int = 0
    least_item: str = ""
    least_qty: int = 999999

    for item, quantity in inventory.items():
        if quantity > most_qty:
            most_qty = quantity
            most_item = item
        if quantity < least_qty:
            least_qty = quantity
            least_item = item

    print(f"Most abundant: {most_item} ({most_qty} units)")
    least_unit_text = "unit" if least_qty == 1 else "units"
    print(f"Least abundant: {least_item} ({least_qty} {least_unit_text})")

    print("\n=== Item Categories ===")

    categories: dict[str, dict[str, int]] = {
            'Abundant': {},
            'Moderate': {},
            'Scarce': {}
            }

    for item, quantity in inventory.items():
        if quantity >= 10:
            categories['Abundant'][item] = quantity
        elif quantity >= 5:
            categories['Moderate'][item] = quantity
        else:
            categories['Scarce'][item] = quantity

    if categories['Abundant']:
        print(f"Abundant: {categories['Abundant']}")
    if categories['Moderate']:
        print(f"Moderate: {categories['Moderate']}")
    if categories['Scarce']:
        print(f"Scarce: {categories['Scarce']}")

    print("\n=== Management Suggestions ===")
    restock = []
    for item, quantity in inventory.items():
        if quantity <= 1:
            restock.append(item)

    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("No restock needed.")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")


if __name__ == "__main__":
    inventory_system()
