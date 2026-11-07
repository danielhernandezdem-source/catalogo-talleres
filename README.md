# catalogo-talleres

Catálogo web de talleres de mecánica. MVP construido con un monolito ligero en Python,
operado con agentes de código siguiendo el **ciclo-producto** (persistencia + trazabilidad + gates).

## Empezar aquí

1. **`INICIO.md`** — el prompt de arranque: pégaselo al agente de código (o dile "lee INICIO.md").
2. **`AGENTS.md`** — la constitución del repo: cómo se trabaja, gates, ambientes. Todo agente la lee.
3. **`docs/fases.md`** — las fases de la iniciativa. Solo se trabaja la fase activa.

## El pack (mapa rápido)

| Carpeta | Qué vive ahí |
|---|---|
| `docs/product.md` | qué es el producto, para quién, qué NO es |
| `docs/tech.md` | stack, versiones, prohibiciones |
| `docs/decisions/` | decisiones CERRADAS (ADRs, inmutables) |
| `docs/debates.md` | decisiones ABIERTAS o diferidas |
| `docs/fases.md` | fases de la iniciativa y su criterio de salida |
| `docs/metricas.md` | cómo medimos si el proceso funciona |
| `backlog/` | necesidades brutas (NB-NNN) |
| `features/F-NNN-slug/` | spec.md (contrato) + bitacora.md (estado, verificaciones, handoff) |
| `features/archived/` | features completadas |
| `_templates/` | plantillas de todos los artefactos |
| `tests/behavior/` | tests derivados de los specs (se escriben antes del código) |

## Ciclo de vida

```
NB (backlog) → spec borrador → [GATE C1: humano aprueba el spec] → en ejecución
  → [CI/tests verdes por tarea] → verificada e2e en dev → [GATE C2: humano cierra] → completada → archived/
```

Cada transición se registra en la bitácora de la feature con fecha, evidencia y quién aprobó.

## Comandos

```bash
uv venv --python 3.12          # una sola vez
uv pip install -r requirements.txt
uv run python manage.py migrate
uv run python manage.py runserver     # la app en http://127.0.0.1:8000
uv run pytest                         # tests
uv run ruff check .                   # lint
git config core.hooksPath .githooks   # una vez por clon: activa el guardián del pack
uv run python ci/check_pack.py        # integridad del pack (también corre en cada commit)
```
