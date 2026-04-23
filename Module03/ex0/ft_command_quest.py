import sys


def display_arguments() -> None:
    arguments: int = len(sys.argv)
    print("=== Command Quest ===")
    if arguments == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if arguments > 1:
        print(f"Arguments received: {arguments - 1}")
        for num in range(1, arguments):
            print(f"Argument {num}: {sys.argv[num]}")
    print(f"Total arguments: {arguments}")


if __name__ == "__main__":
    display_arguments()
