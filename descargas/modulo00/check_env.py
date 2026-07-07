"""Sanity check for MATE-2105 Module 0.

Run from the modulo00_arranque directory:

    python scripts/check_env.py
"""

from __future__ import annotations

import platform


def main() -> None:
    import numpy as np
    import pandas as pd
    import sklearn
    from sklearn.datasets import load_wine

    data = load_wine(as_frame=True)
    x = data.data
    y = data.target
    counts = y.value_counts().sort_index().to_dict()

    assert x.shape == (178, 13), f"Unexpected X shape: {x.shape}"
    assert y.shape == (178,), f"Unexpected y shape: {y.shape}"
    assert counts == {0: 59, 1: 71, 2: 48}, f"Unexpected class counts: {counts}"

    print(f"Python: {platform.python_version()}")
    print(f"numpy: {np.__version__}")
    print(f"pandas: {pd.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print(f"Dataset wine: {x.shape[0]} observaciones, {x.shape[1]} variables")
    print(f"Conteo por clase: {counts}")
    print("Chequeo completado correctamente.")


if __name__ == "__main__":
    main()
