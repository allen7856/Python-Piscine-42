import sys
import importlib


def check_dependencies() -> bool:
    # check if all required packages are installed
    required = {
            'pandas': 'pandas',
            'numpy': 'numpy',
            'matplotlib': 'matplotlib.pyplot',
            'requests': 'requests',
    }
    all_ok: bool = True

    print("Checking dependencies:")
    for package, module in required.items():
        mod = importlib.import_module(module)
        version = getattr(mod, '__version__', 'unknown')
        print(f"[OK] {package} ({version}) - "
              f"{package.capitalize()} ready")
        except ImportError:
            print(f"[MISSING] {package} - not installed")
            print(f"Install with: pip install {package}")
            all_ok = False

    return all_ok


def analyze_matrix_data() -> None:
    # using numpy and pandas
    import numpy as np
    import pandas as pd
