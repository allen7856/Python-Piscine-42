import sys
import os
import site


def check_virtual_environment() -> None:
    # sys.prefix points to venv or system
    # sys.base_prefix always points to system
    # if they're different, we're inside a virtual environment
    in_venv: bool = sys.prefix != sys.base_prefix

    if in_venv:
        # full path to the venv folder
        venv_path: str = sys.prefix
        # just the name of the folder
        venv_name: str = os.path.basename(venv_path)
        # where the python binary is (inside venv)
        python_path: str = sys.executable
        # returns the first of a list of folders where pip install packages
        packages_path: str = site.getsitepackages()[0]

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environmental Path: {venv_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(packages_path)

    else:
        # where the python binary is (outside venv)
        python_path: str = sys.executable

        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print("\nThen run this program again")


if __name__ == "__main__":
    check_virtual_environment()
