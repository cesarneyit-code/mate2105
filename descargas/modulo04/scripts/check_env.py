#!/usr/bin/env python3
from __future__ import annotations

import importlib


REQUIRED = ["numpy", "pandas", "sklearn", "matplotlib", "seaborn", "nbformat"]


def main() -> int:
    missing = []
    for package in REQUIRED:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "sin version")
            print(f"ok {package}: {version}")
        except Exception as exc:
            missing.append((package, str(exc)))
            print(f"falta {package}: {exc}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

