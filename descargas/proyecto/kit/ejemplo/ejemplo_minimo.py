"""Ejemplo reproducible del formato de resultados del proyecto.

El objetivo es mostrar la estructura baseline -> modelo -> artefacto. El caso
`load_wine` es didáctico y no constituye por sí solo una propuesta aplicada.
"""

from __future__ import annotations

import json
from pathlib import Path

from sklearn.datasets import load_wine
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


SEED = 2105


def summarize(y_true, y_pred) -> dict[str, object]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro")),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }


def main() -> None:
    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=SEED,
        stratify=y,
    )

    models = {
        "baseline_most_frequent": DummyClassifier(strategy="most_frequent"),
        "logistic_scaled": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "model",
                    LogisticRegression(max_iter=2000, random_state=SEED),
                ),
            ]
        ),
    }

    results: dict[str, object] = {
        "dataset": "sklearn.datasets.load_wine",
        "seed": SEED,
        "split": {"test_size": 0.25, "stratified": True},
        "models": {},
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        results["models"][name] = summarize(y_test, model.predict(X_test))

    output = Path(__file__).resolve().parent / "metrics_ejemplo.json"
    output.write_text(
        json.dumps(results, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nArtefacto escrito en: {output}")


if __name__ == "__main__":
    main()
