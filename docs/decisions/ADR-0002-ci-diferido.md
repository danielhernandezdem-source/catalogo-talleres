# ADR-0002: CI/CD diferido hasta después del MVP

- fecha:: 2026-11 · estado:: aceptada · decidida-por:: Kevin
- tipo:: proceso · origen:: arranque (Fase 0)

## Contexto
MVP en local, sin hosting. Automatizar CI/CD ahora sería infraestructura sin usuario.

## Opciones consideradas
1. **GitHub Actions desde el día 1** — pro: gratis, gate físico en la nube. contra: prematuro.
2. **Ninguno por ahora** — pro: cero configuración, foco en el producto. contra: los gates
   dependen de disciplina local (mitigado: el chequeo de consistencia los exige).

## Decisión
Opción 2. Gates físicos en local (pytest + ruff + manage.py check). Revisar tras el MVP
(registrado en `docs/debates.md` D-001).

## Consecuencias
- `ci/ci-futuro.md` queda como marcador de intención (no activo). Nota (2026-11): no vive
  bajo `.github/workflows/` porque GitHub exige el scope `workflow` en el token para
  escribir CUALQUIER archivo en esa ruta — y el MVP no necesita ese permiso.
- Cuando se active, los mismos comandos locales se convierten en el workflow.
