class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print("\nInvalid operation attempted: height -5cm [REJECTED]")
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")
