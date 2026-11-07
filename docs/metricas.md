# Métricas del proceso (¿funciona el ciclo-producto?)

Línea base: se fija la primera vez que se cierre una feature. Revisión cada 2 semanas.
Fuente de datos: `git log` + bitácoras de `features/` — nada extra que instalar.

| # | Métrica | Cómo se colecta | Qué significa |
|---|---|---|---|
| 1 | **Retrabajo** | commits `fix(F-NNN)` en los 14 días posteriores al cierre de esa feature | si sube, los specs están flojos o los tests no cubren |
| 2 | **Defectos escapados** | bugs hallados después del cierre (lista abajo) | la señal más honesta de calidad |
| 3 | **Ciclo** | días entre `NB aprobada` y `completada` (historia de la bitácora) | velocidad real, no percepción |
| 4 | **Continuidad** | % de sesiones que inician con consistencia PASS sin preguntar qué sigue | mide el handoff / contexto mínimo viable |
| 5 | **Evidencia** | % de features cerradas con registro de verificaciones completo | si baja, el proceso se está saltando gates |

## Registro de revisión

| fecha | M1 | M2 | M3 | M4 | M5 | lectura |
|---|---|---|---|---|---|---|

## Defectos escapados (bitácora viva)
- (ninguno aún)
