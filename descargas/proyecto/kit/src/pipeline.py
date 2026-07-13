"""Utilidades mínimas para un proyecto MATE-2105.

Adapta estas funciones al tipo de problema. No copies una métrica o una
partición sin justificarla en el reporte.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


SEED = 2105


def set_seed(seed: int = SEED) -> None:
    """Fija las fuentes de aleatoriedad usadas por este archivo."""
    random.seed(seed)
    np.random.seed(seed)


def split_supervised(
    X: Any,
    y: Any,
    *,
    test_size: float = 0.20,
    stratify: bool = False,
    seed: int = SEED,
) -> tuple[Any, Any, Any, Any]:
    """Crea una partición reproducible; adapta el método a datos temporales o agrupados."""
    stratification = y if stratify else None
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=seed,
        stratify=stratification,
    )


def classification_metrics(y_true: Any, y_pred: Any) -> dict[str, float]:
    """Métricas de referencia para clasificación; el proyecto debe declarar una principal."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro")),
    }


def regression_metrics(y_true: Any, y_pred: Any) -> dict[str, float]:
    """Métricas de referencia para regresión."""
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred) ** 0.5),
    }


def write_json(payload: dict[str, Any], path: str | Path) -> None:
    """Escribe un artefacto JSON estable y legible."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
