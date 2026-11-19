# Debates — decisiones abiertas o diferidas

Una entrada por tema. Cuando se decide, se promueve a `docs/decisions/ADR-NNNN` y aquí
queda el enlace. Estado: `propuesta | en-discusion | diferida | decidida`.

## D-001 — CI/CD en la nube
- estado:: **diferida** · fecha:: 2026-11 · decidida-por:: Kevin
- Contexto: máquina modesta y MVP local; CI/CD prematuro.
- Opciones: (a) GitHub Actions (gratis, corre fuera de la PC) / (b) ninguno por ahora.
- Decisión: **(b) ninguno por ahora**. Los gates físicos corren en local (pytest + ruff + manage.py check).
- Revisar cuando: exista hosting o el dueño commitee sin supervisión.

## D-002 — Búsqueda sin acentos (cadencia de texto)
- estado:: **en-discusion** · fecha:: 2026-11 · decidida-por:: pendiente
- Contexto: `home` filtra con `icontains` sobre nombre y ciudad. SQLite es insensible a
  mayúsculas pero NO a acentos: `?q=rapido` no encuentra "El Rápido Lubricentro".
  Verificado en local (2026-11): `?q=Santiago` → 2 resultados; `?q=rapido` → 0.
- Opciones: (a) ignorar acentos en SQL (función/regex) / (b) normalizar al guardar y al
  buscar (quitar tildes en ambos lados) / (c) dejarlo así.
- Decisión: **pendiente** — se aborda en Fase 2 (Descubrimiento: búsqueda por servicio/marca).
- Revisar cuando: se trabaje Fase 2, o antes si el dueño lo nota.

## D-003 — Base de datos en el repositorio
- estado:: **decidida** · fecha:: 2026-11 · decidida-por:: Daniel
- Contexto: `db.sqlite3` estaba en `.gitignore`, así que un clon fresco arrancaba vacío
  y el handoff de F-000 ("3 talleres de demo") no era reproducible.
- Opciones: (a) versionar la DB / (b) fixture o script de seed documentado.
- Decisión: **(a) versionar la DB**, a sabiendas de que es una mala idea a mediano plazo.
  Alternativa (b) pendiente como deuda.
- Consecuencias: el clon fresco ve el catálogo; pero dos ediciones concurrentes generan
  conflicto binario en git, y la contraseña del superusuario de demo queda en el repo.
- Revisar cuando: haya dos personas editando datos a la vez, o antes de Fase 3
  (inscripción de talleres).
