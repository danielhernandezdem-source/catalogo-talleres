# Fases de la iniciativa

Regla del ciclo aplicada a fases: **no se abre la fase N+1 sin cerrar la salida de la N**
(cada cierre de fase se registra con fecha en la historia de abajo).

## Fase 0 — Andamio (ACTIVA)
- Alcance: repo con el pack completo, Django funcionando, un modelo mínimo (Taller),
  página de inicio con listado y búsqueda por nombre, tests de comportamiento verdes en local.
- Salida (gate): `pytest` verde + la app corre en `runserver` + el pack documentado.

## Fase 1 — Catálogo MVP
- Alcance: CRUD completo de talleres por el administrador (Django admin), ficha pública del
  taller, búsqueda por nombre y ciudad, roles mínimos (explicar en simple antes de decidir).
- Salida: 10 talleres reales cargados, búsqueda útil, CRUD operado por el dueño.

## Fase 2 — Descubrimiento
- Alcance: búsqueda por servicio/marca, filtros, ficha enriquecida (fotos, horarios completos).
- Salida: un visitante encuentra taller por servicio sin ayuda.

## Fase 3 — Adopción
- Alcance: inscripción de taller por el propio dueño (formulario público con moderación).
- Salida: 1 taller real inscrito por su propio dueño, aprobado por el administrador.

---

## Historia de fases
| fecha | fase | evento | evidencia |
|---|---|---|---|
| 2026-11 | 0 | iniciada | commit del andamio |
