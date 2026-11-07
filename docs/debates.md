# Debates — decisiones abiertas o diferidas

Una entrada por tema. Cuando se decide, se promueve a `docs/decisions/ADR-NNNN` y aquí
queda el enlace. Estado: `propuesta | en-discusion | diferida | decidida`.

## D-001 — CI/CD en la nube
- estado:: **diferida** · fecha:: 2026-11 · decidida-por:: Kevin
- Contexto: máquina modesta y MVP local; CI/CD prematuro.
- Opciones: (a) GitHub Actions (gratis, corre fuera de la PC) / (b) ninguno por ahora.
- Decisión: **(b) ninguno por ahora**. Los gates físicos corren en local (pytest + ruff + manage.py check).
- Revisar cuando: exista hosting o el dueño commitee sin supervisión.
