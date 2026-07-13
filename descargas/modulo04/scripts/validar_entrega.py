#!/usr/bin/env python3
"""Valida estructura y ejecución visible de un laboratorio MATE-2105."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import nbformat


LABS = {
    "lab01": {"cell": "lab01_interpretacion", "fragment": "lab01_regresion_gradiente", "words": [80, 140]},
    "lab02": {"cell": "lab02_recomendacion", "fragment": "lab02_regularizacion_clasificacion", "words": [100, 160]},
    "lab03": {"cell": "lab03_diagnostico", "fragment": "lab03_redes_desde_cero", "words": [100, 160]},
    "lab04": {"cell": "lab04_diagnostico", "fragment": "lab04_diagnostico_modelos", "words": [110, 170]},
    "lab05": {"cell": "lab05_interpretacion", "fragment": "lab05_no_supervisado", "words": [120, 180]},
}
MARKER = re.compile(r"<!--\s*MATE2105:MANUAL_RESPONSE\s+id=([A-Za-z0-9_-]+)\s*-->", re.I)
WORDS = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+(?:[-'][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+)*")


def role(cell: Any) -> str | None:
    mate = cell.get("metadata", {}).get("mate2105", {})
    return mate.get("role") if isinstance(mate, dict) else None


def manual_answer(notebook: Any, expected_id: str) -> tuple[str, int]:
    matches = []
    for cell in notebook.cells:
        if cell.cell_type != "markdown":
            continue
        mate = cell.get("metadata", {}).get("mate2105", {})
        tags = set(cell.get("metadata", {}).get("tags", []))
        marker = MARKER.search(cell.source)
        if (
            isinstance(mate, dict) and mate.get("id") == expected_id
            or "mate2105-manual-response" in tags
            or marker and marker.group(1) == expected_id
        ):
            matches.append(cell)
    if len(matches) != 1:
        return "", len(matches)
    text = MARKER.sub("", matches[0].source)
    text = re.sub(r"(?is)^.*?\*\*Tu respuesta[^\n]*\*\*\s*", "", text).strip()
    if text.lower().startswith("[escribe aquí"):
        text = ""
    return text, 1


def validate(path: Path) -> dict[str, Any]:
    result = {"path": str(path), "valid": False, "errors": [], "warnings": [], "facts": {}}
    try:
        notebook = nbformat.read(path, as_version=4)
    except Exception as exc:
        result["errors"].append(f"No se pudo leer el notebook: {exc}")
        return result
    metadata = notebook.metadata.get("mate2105", {})
    assignment = metadata.get("assignment_id") if isinstance(metadata, dict) else None
    if assignment not in LABS:
        result["errors"].append("Falta un `assignment_id` válido en los metadatos MATE-2105.")
        return result
    contract = LABS[assignment]
    if metadata.get("schema_version") != "1.0":
        result["errors"].append("El notebook no usa el esquema MATE-2105 1.0.")
    if contract["fragment"] not in path.stem:
        result["warnings"].append(f"El nombre debería contener `{contract['fragment']}`.")
    answer, matches = manual_answer(notebook, contract["cell"])
    if matches != 1:
        result["errors"].append(f"Se encontraron {matches} celdas de respuesta manual; debe haber una.")
    if not answer:
        result["errors"].append("La respuesta manual está vacía.")
    count = len(WORDS.findall(answer))
    minimum, maximum = contract["words"]
    if answer and not minimum <= count <= maximum:
        result["warnings"].append(f"La respuesta tiene {count} palabras; se sugieren {minimum}-{maximum}.")
    relevant = [
        cell for cell in notebook.cells
        if cell.cell_type == "code" and role(cell) in {"student_code", "structured_response", "evidence"}
    ]
    unfinished = sum(
        "NotImplementedError" in cell.source or bool(re.search(r"(?im)^\s*#\s*TODO\b", cell.source))
        for cell in relevant
    )
    unexecuted = sum(cell.source.strip() != "" and cell.execution_count is None for cell in relevant)
    output_errors = sum(
        output.get("output_type") == "error"
        for cell in notebook.cells if cell.cell_type == "code"
        for output in cell.get("outputs", [])
    )
    if unfinished:
        result["errors"].append(f"Quedan {unfinished} celdas con TODO o NotImplementedError.")
    if unexecuted:
        result["warnings"].append(f"Hay {unexecuted} celdas de respuesta sin ejecutar.")
    if output_errors:
        result["errors"].append(f"El notebook conserva {output_errors} salidas de error.")
    result["facts"] = {
        "assignment_id": assignment,
        "manual_word_count": count,
        "unfinished_cells": unfinished,
        "unexecuted_response_cells": unexecuted,
        "error_outputs": output_errors,
    }
    result["valid"] = not result["errors"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebooks", nargs="*", type=Path)
    parser.add_argument("--buscar", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    paths = list(args.notebooks)
    if args.buscar:
        paths.extend(sorted(args.buscar.rglob("*.ipynb")))
    paths = sorted(set(path.resolve() for path in paths if ".ipynb_checkpoints" not in path.parts))
    if not paths:
        print("ERROR: no se encontraron notebooks.", file=sys.stderr)
        return 2
    reports = [validate(path) for path in paths]
    payload = {"valid": all(item["valid"] for item in reports), "notebooks": reports}
    if args.json:
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for report in reports:
        status = "OK" if report["valid"] else "ERROR"
        print(f"{status}: {report['path']}")
        for message in report["errors"]:
            print(f"  ERROR: {message}")
        for message in report["warnings"]:
            print(f"  AVISO: {message}")
    return 0 if payload["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
