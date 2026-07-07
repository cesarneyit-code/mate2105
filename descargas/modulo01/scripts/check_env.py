#!/usr/bin/env python3
from __future__ import annotations

import importlib
import sys


REQUIRED = ["numpy", "pandas", "sklearn", "matplotlib", "seaborn", "nbformat"]


def main() -> int:
    print(f"Python: {sys.version.split()[0]}")
    for name in REQUIRED:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "ok")
        print(f"{name}: {version}")
    from sklearn.datasets import load_breast_cancer, load_diabetes

    diabetes = load_diabetes()
    cancer = load_breast_cancer()
    print(f"diabetes: X={diabetes.data.shape}, y={diabetes.target.shape}")
    print(f"breast_cancer: X={cancer.data.shape}, y={cancer.target.shape}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
