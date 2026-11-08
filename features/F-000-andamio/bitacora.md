- title:: F-000-andamio — bitácora
- tipo:: [[bitacora-feature]] · feature:: F-000 · estado:: verificada-e2e
- origen:: decisión de arranque · rama:: main (andamio inicial) · ambiente:: dev (local)
- head:: 7ae3b83 · actualizado:: 2026-11

## Historia del ciclo
| fecha | de → a | evidencia | gate |
|---|---|---|---|
| 2026-11 | borrador → en-ejecucion | commits e5c4777/d24e90c/299ef1e | C1: Kevin aprueba el andamio |
| 2026-11 | en-ejecucion → verificada-e2e | verificaciones V1-V4 abajo | gates físicos en verde |

## Plan (bloques ejecutables)
1. ✅ Estructura del pack (driven) con plantillas materializadas
2. ✅ Django + SQLite + app `taller` con migración y admin
3. ✅ Home con listado y búsqueda + tests de comportamiento
4. ✅ Guardián de integridad del pack con hook pre-commit

## Registro de verificaciones
| fecha | tipo | qué corrió | ambiente | resultado | evidencia | aprobó |
|---|---|---|---|---|---|---|
| 2026-11 | gate F (CI local) | `uv run pytest -q` | dev | PASS 2/2 | pytest exit 0 | — |
| 2026-11 | gate F (CI local) | `uv run ruff check .` | dev | PASS | "All checks passed!" | — |
| 2026-11 | gate F (CI local) | `uv run python manage.py check` | dev | PASS | 0 issues | — |
| 2026-11 | gate F (CI local) | clon fresco: venv+install+migrate+pytest+ruff | clone-test | PASS completo | "2 passed" en clon sin db | — |
| 2026-11 | prueba e2e | `runserver` + curl home y `/admin/` | dev | PASS HTTP 200 ambos | catálogo con 3 talleres de demo | — |
| 2026-11 | prueba e2e | servidor del CLON fresco en :8124 | clone-test | PASS HTTP 200 | enciende sin pasos ocultos | — |

## Decisiones tomadas durante la feature
- (2026-11, técnica) Stack Django 5.2 LTS + SQLite + HTMX/Bootstrap CDN → ADR-0001
  (alternativas descartadas: FastAPI+JS, Flask)
- (2026-11, proceso) CI/CD diferido hasta después del MVP → ADR-0002
- (2026-11, proceso) Guardián de integridad + hook pre-commit → ADR-0003

## Aprendí (explicaciones para el dueño)
- **Encender la app**: `uv run python manage.py runserver` levanta un servidor de prueba
  en tu propia máquina (no es internet). Luego abres `http://127.0.0.1:8000` en el navegador.
- **El admin**: `http://127.0.0.1:8000/admin/` es un panel que Django regala: ahí creas,
  editas y borras talleres sin escribir código. Entrar requiere un superusuario
  (`uv run python manage.py createsuperuser`).
- **Los tests** (`uv run pytest`) son un robot que revisa la app por ti: si algo se rompe,
  los tests te dicen QUÉ se rompió antes de que lo vea un visitante.
- **El clon fresco**: probamos que alguien que descargue el repo por primera vez pueda
  encender todo con 4 comandos y cero adivinanzas.

## Commits
- `e5c4777` chore: iniciar repositorio (vacío)
- `d24e90c` docs: pack ciclo-producto (driven)
- `299ef1e` feat: andamio Django 5.2 LTS + SQLite (Fase 0)
- `7ae3b83` feat: guardián de integridad del pack

## Lecciones (→ reusar en el proyecto)
- Verificar rutas con git: usar rutas nativas `C:/...` (las `/c/...` no las traduce git en Windows).
- Un clon fresco como prueba final del andamio: detecta pasos ocultos no documentados.

## Handoff (contexto mínimo viable)
- HEAD: `7ae3b83` · working tree: limpio (local, sin push)
- Estado: Fase 0 completa y verificada. Datos de demo cargados (3 talleres, superusuario `admin`).
- Siguiente acción: Kevin da la URL del remoto → push de `main` → crear `dev`. Después,
  primera feature real (F-001) siguiendo INICIO.md en un chat nuevo.
