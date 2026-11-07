#!/usr/bin/env python3
"""Pack integrity guard (ciclo-producto).

Detects accidental damage to the driven pack: deleted files, missing required
sections, and edits to immutable (accepted) ADRs. Runs as a pre-commit hook and
as step 0 of the consistency check.

Usage:
    uv run python ci/check_pack.py                 # check (exit 0 = OK)
    uv run python ci/check_pack.py --update-index  # regenerate the ADR hash index

Why: agents have full write access to the working tree and sometimes rewrite or
empty context files. Git makes damage recoverable; this guard makes it VISIBLE
and blocks it at commit time.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    "AGENTS.md",
    "INICIO.md",
    "README.md",
    "docs/product.md",
    "docs/tech.md",
    "docs/fases.md",
    "docs/metricas.md",
    "docs/debates.md",
    "docs/decisions",
    "docs/decisions/INDEX.md",
    "backlog",
    "features",
    "features/archived",
    "_templates/README.md",
    "_templates/backlog.md",
    "_templates/spec.md",
    "_templates/bitacora.md",
    "_templates/adr.md",
    "tests/behavior",
    "requirements.txt",
    "manage.py",
    "pytest.ini",
    "ruff.toml",
]

REQUIRED_SECTIONS = {
    "AGENTS.md": ["## Gates del proyecto", "## Ambientes y ramas", "## Reglas duras"],
    "INICIO.md": [
        "## Paso 0",
        "## Ciclo por feature",
        "## Regla de decisión por defecto (MVP)",
        "## Escalación obligatoria a Kevin",
        "## Manejo de contexto",
        "## Nunca",
    ],
    "docs/fases.md": ["## Fase 0", "## Historia de fases"],
    "docs/metricas.md": ["## Registro de revisión"],
    "_templates/bitacora.md": ["## Registro de verificaciones", "## Handoff"],
    "_templates/spec.md": ["## Qué NO debe hacer", "## Comportamientos de error"],
}


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_index() -> dict[str, str]:
    index_path = ROOT / "docs" / "decisions" / "INDEX.md"
    hashes: dict[str, str] = {}
    if not index_path.exists():
        return hashes
    for line in index_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- ") and len(line.split()) >= 3:
            _, digest, filename = line.split(maxsplit=2)
            hashes[filename] = digest
    return hashes


def update_index() -> int:
    index_path = ROOT / "docs" / "decisions" / "INDEX.md"
    lines = [
        "# Índice de integridad de ADRs",
        "",
        "Los ADRs aceptados son inmutables: este índice guarda su huella sha256.",
        "Regenerar tras aceptar un ADR nuevo:",
        "`uv run python ci/check_pack.py --update-index`",
        "",
    ]
    adrs = sorted((ROOT / "docs" / "decisions").glob("ADR-*.md"))
    for adr in adrs:
        lines.append(f"- {sha256_of(adr)} {adr.name}")
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"INDEX actualizado: {len(adrs)} ADRs registrados")
    return 0


def main() -> int:
    if "--update-index" in sys.argv:
        return update_index()

    errors: list[str] = []

    # 1) Required paths exist
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"FALTA: {rel}")

    # 2) Required sections in protected documents
    for rel, markers in REQUIRED_SECTIONS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"SECCIÓN FALTANTE en {rel}: {marker}")

    # 3) Every feature bitácora keeps its core sections
    for bitacora in sorted(ROOT.glob("features/F-*/bitacora.md")):
        text = bitacora.read_text(encoding="utf-8")
        rel = bitacora.relative_to(ROOT).as_posix()
        for marker in ("## Registro de verificaciones", "## Handoff"):
            if marker not in text:
                errors.append(f"SECCIÓN FALTANTE en {rel}: {marker}")

    # 4) Accepted ADRs are immutable (hash index)
    index = load_index()
    adr_dir = ROOT / "docs" / "decisions"
    for adr in sorted(adr_dir.glob("ADR-*.md")):
        expected = index.get(adr.name)
        actual = sha256_of(adr)
        if expected is None:
            errors.append(
                f"ADR sin registrar en INDEX: {adr.name} "
                "(corre: uv run python ci/check_pack.py --update-index)"
            )
        elif expected != actual:
            errors.append(f"ADR MODIFICADO tras ser aceptado: {adr.name}")
    for filename in index:
        if not (adr_dir / filename).exists():
            errors.append(f"ADR ELIMINADO pero sigue en INDEX: {filename}")

    if errors:
        print("PACK DAÑADO — corrige o restaura antes de continuar:")
        for error in errors:
            print(f"  - {error}")
        print("Restaurar un archivo:  git checkout HEAD -- <ruta>")
        return 1

    print("PACK: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
