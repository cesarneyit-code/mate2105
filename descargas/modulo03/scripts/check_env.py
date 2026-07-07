#!/usr/bin/env python3
from __future__ import annotations

import importlib


REQUIRED = ["numpy", "pandas", "sklearn", "matplotlib", "nbformat"]


def main() -> int:
    ok = True
    for name in REQUIRED:
        try:
            importlib.import_module(name)
            print(f"ok: {name}")
        except Exception as exc:
            print(f"faltante: {name} ({exc})")
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
