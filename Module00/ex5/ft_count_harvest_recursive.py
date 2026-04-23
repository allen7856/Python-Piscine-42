def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    count_helper(1, days)
    print("Harvest time!")


def count_helper(current: int, days: int) -> None:
    if current > days:
        return
    print("Day", current)
    count_helper(current + 1, days)
