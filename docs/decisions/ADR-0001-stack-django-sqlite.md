# ADR-0001: stack Django + SQLite + HTMX (monolito, sin Node)

- fecha:: 2026-11 · estado:: aceptada · decidida-por:: Kevin
- tipo:: técnica · origen:: arranque del proyecto (Fase 0)

## Contexto
Máquina modesta (Lubuntu LTS, dual core, 3 GB RAM), desarrollador principiante, producto
MVP de cero. Se necesita stack que corra fluido en esa máquina y que el dueño pueda entender.

## Opciones consideradas
1. **Django + HTMX + SQLite** — pro: admin gratis (CRUD sin frontend), ORM + migraciones,
   auth incluida, un solo proceso, sin build de JS, migración a Postgres trivial después.
   contra: monolito (para MVP es una virtud).
2. **FastAPI + frontend JS** — pro: moderno, API-first. contra: sin admin, sin templates,
   exige montar frontend aparte (Node), más piezas que mantener.
3. **Flask + extensiones** — pro: mínimo. contra: todo se arma a mano (auth, admin, migraciones):
   peor para un principiante.

## Decisión
Opción 1. Django 5.2 LTS + SQLite + HTMX/Bootstrap por CDN, venv con uv, pytest + ruff.

## Consecuencias
- El CRUD administrativo existe casi sin escribir código (Django admin).
- Migrar a Postgres después = cambiar engine en settings + migraciones.
- Prohibido Node/npm y Docker (ver docs/tech.md) hasta decisión escalada.
