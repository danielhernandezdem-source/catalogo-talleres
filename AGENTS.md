# AGENTS.md — catalogo-talleres

## Qué es este proyecto

Catálogo web de talleres de mecánica (MVP). El dueño del producto es un desarrollador
principiante: **explica en lenguaje simple cada decisión** (ver regla final).

## Entorno y comandos de verificación (correr SIEMPRE antes de decir "listo")

- Python vía uv (venv en `.venv/`): `uv venv --python 3.12` y `uv pip install -r requirements.txt` (una vez).
- Lint: `uv run ruff check .`
- Tests: `uv run pytest` (los de comportamiento viven en `tests/behavior/`)
- Django checks: `uv run python manage.py check`
- App local: `uv run python manage.py runserver` → http://127.0.0.1:8000

## Mapa del pack (empezar SIEMPRE por aquí)

1. Lee `docs/product.md` (qué es) y `docs/tech.md` (stack y prohibiciones).
2. Lee `docs/fases.md`: **solo se trabaja la fase activa**. No se abre la siguiente sin cerrar su salida.
3. Lee la bitácora de la feature activa en `features/F-NNN-*/bitacora.md` — ahí vive el estado,
   las decisiones y el handoff (contexto mínimo viable).
4. Usa las plantillas de `_templates/` para crear artefactos nuevos. Nunca improvises la estructura.

## Gates del proyecto

**Físicos** (corren solos, ahora en local): `pytest` + `ruff check` + `manage.py check` antes de
cada cierre de tarea. El CI/CD en la nube está **diferido a decisión explícita** (ver `docs/debates.md`);
hasta entonces NADA se automatiza en la nube sin aprobarlo.

**Conceptuales** (humano registrado en el registro de verificaciones de la bitácora):
- **C1**: aprobar el spec antes de codificar → Kevin (o el dueño con Kevin presente)
- **C2**: cerrar/promover la feature → Kevin
- Cambios de stack, dependencias nuevas, auth/pagos/datos personales → **escalar a Kevin** (ver INICIO.md)

## Ambientes y ramas

| rama | ambiente | regla |
|---|---|---|
| `feature/F-NNN-*` | dev (local) | iteración libre + verificaciones locales |
| `dev` | integración y pruebas | merge solo cuando la feature está probada |
| `main` | liberación | merge solo tras C2; es lo que se mostraría al público |

Hoy todo corre en local (SQLite). No hay despliegue externo: decidirlo es una escalación.

## Reglas duras

- Empieza cada sesión con el **chequeo de consistencia**: HEAD de la bitácora vs `git log`,
  commits reflejados, estados vs evidencia, handoff fresco. No continúes sobre un estado falso.
- Nunca declares "listo" sin handoff actualizado y consistencia PASS.
- Código y comentarios en inglés; commits, specs y documentación en español.
- Commits con prefijo amarrado al ciclo: `feat(F-NNN):`, `test(F-NNN):`, `fix(F-NNN):`, `docs(F-NNN):`, `gate(F-NNN):`.
- La actualización de la bitácora va EN el mismo commit que el cambio de código.
- Al cerrar una feature probada (feature + dev), **recomienda abrir un chat nuevo** (manejo de
  contexto) y deja el handoff listo para retomar.
- Prohibido: Node/npm, Docker, servicios en la nube, credenciales en el código. Decisiones sobre
  esto = escalación, no decisión propia.
- Si falta información del dueño (negocio o preferencias), **pregúntale en lenguaje simple**; si la
  pregunta es técnica compleja, escala a Kevin.

## Cómo explicar (para que el dueño aprenda)

Al final de cada bloque de trabajo agrega en la bitácora, sección **"Aprendí"**, 3-5 líneas en
lenguaje simple: qué se hizo, por qué, y un concepto nuevo explicado con ejemplo (ej.: "un modelo
es la tabla de la base de datos y sus reglas"). Sin jerga sin traducir.
