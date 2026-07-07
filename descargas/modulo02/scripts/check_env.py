#!/usr/bin/env python3
from __future__ import annotations

import importlib


REQUIRED = ["numpy", "pandas", "sklearn", "matplotlib", "nbformat"]
OPTIONAL = ["torch"]


def check(name: str) -> bool:
    try:
        importlib.import_module(name)
        print(f"ok: {name}")
        return True
    except Exception as exc:
        print(f"faltante: {name} ({exc})")
        return False


def main() -> int:
    ok = True
    for name in REQUIRED:
        ok = check(name) and ok
    for name in OPTIONAL:
        check(name)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
