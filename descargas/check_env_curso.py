#!/usr/bin/env python3
"""Comprueba el entorno semestral offline de MATE-2105."""

from __future__ import annotations

import platform
import sys
from importlib.metadata import PackageNotFoundError, version


SUPPORTED_PYTHON = {(3, 11), (3, 12)}
PACKAGES = (
    "numpy",
    "pandas",
    "scipy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "jupyterlab",
    "notebook",
    "ipykernel",
    "nbformat",
    "joblib",
    "torch",
    "websocket-client",
    "beautifulsoup4",
)


def package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError as exc:
        raise RuntimeError(f"Falta el paquete {name!r}.") from exc


def main() -> int:
    py = sys.version_info[:2]
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")
    if py not in SUPPORTED_PYTHON:
        supported = "3.11 o 3.12"
        raise RuntimeError(
            f"Este curso se probó con Python {supported}; se encontró "
            f"{platform.python_version()}. Crea el entorno con una versión compatible."
        )

    for package in PACKAGES:
        print(f"{package}: {package_version(package)}")

    import numpy as np
    import torch
    from sklearn.datasets import load_wine
    from sklearn.linear_model import LinearRegression

    X, y = load_wine(return_X_y=True)
    assert X.shape == (178, 13)
    assert np.bincount(y).tolist() == [59, 71, 48]

    X_reg = np.arange(12, dtype=float).reshape(6, 2)
    y_reg = 1.5 + X_reg @ np.array([0.25, -0.1])
    model = LinearRegression().fit(X_reg, y_reg)
    assert np.allclose(model.predict(X_reg), y_reg)

    tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    assert torch.allclose(tensor.mean(), torch.tensor(2.5))

    print("Wine: 178 observaciones, 13 variables, clases [59, 71, 48]")
    print("NumPy, scikit-learn y PyTorch: operación mínima correcta")
    print("Chequeo semestral completado correctamente.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
