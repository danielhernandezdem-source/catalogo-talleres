# Spec: Capa de agente — política de enrutamiento (F-001)

- origen:: [[NB-001]] · estado:: aprobada
- fecha:: 2026-11-19 · aprobada-por:: Kevin (GATE C1, sesión 2026-11-19)

## Qué debe hacer
- El pack debe definir una **política de selección de modelo por tipo de tarea**, con tres
  niveles: FUERTE (criterio: specs, arquitectura, revisión de diff), ILIMITADO (volumen:
  código repetitivo, tests, lectura) y NUNCA SOLO (lo que el dueño no puede verificar).
- La política debe **separarse de la ruta**: el repo define niveles, la config del agente
  define el modelo concreto del día. Ningún nombre de modelo en `docs/agentes.md`.
- Cada feature debe registrar en su bitácora qué modelo se usó por tarea (evidencia).
- Las cuotas de los proveedores se registran como **evidencia viva en la bitácora**, no
  en el documento protegido (caducan; actualizarlas no debe exigir escalación).
- Una tarea que falla dos veces seguidas en nivel ILIMITADO **sube a FUERTE** y se
  registra; si el dueño no entiende una explicación, sube a FUERTE.

## Qué NO debe hacer (fuera de alcance)
- No fija modelos, proveedores ni precios en el repo.
- No agrega gates físicos nuevos al CI (ADR-0002 lo difiere).
- No cambia el ciclo de vida existente ni el formato de las features.

## Comportamientos de error (obligatorios)
- SI una tarea declarada ILIMITADO falla dos veces consecutivas, ENTONCES el agente
  debe repetirla en FUERTE y registrar la escalación en la bitácora.
- SI el guardián (`check_pack.py`) detecta que falta `docs/agentes.md` o sus secciones,
  ENTONCES el commit se rechaza (igual que cualquier archivo del pack).
- SI el dueño no entiende una explicación, ENTONCES la tarea sube a FUERTE antes de
  continuar (sin excepciones "es que era fácil").

## Tests de comportamiento (se escriben ANTES de codificar)
| id | comportamiento | cómo se verifica |
|---|---|---|
| T1 | check_pack falla si `docs/agentes.md` falta o pierde una sección requerida | mover el archivo y correr `uv run python ci/check_pack.py` (debe fallar); restaurar (debe pasar) |
| T2 | `docs/agentes.md` no contiene nombres de modelos/proveedores | `grep -iE "openrouter|nous|gpt|claude|gemini|glm"` → 0 coincidencias |
| T3 | ADR-0004 aceptado e inmutable | huella en `docs/decisions/INDEX.md` + check_pack PASS |
| T4 | Las plantillas nuevas tienen las secciones requeridas | check_pack PASS con secciones agregadas a `REQUIRED_SECTIONS` |

## Verificación end-to-end (paso final del spec)
1. Clon/rama limpia → `git config core.hooksPath .githooks`.
2. `uv run python ci/check_pack.py` → PACK: OK (con el doc nuevo y el ADR registrado).
3. T1 y T2 ejecutados con resultado registrado en la bitácora.
4. Commit `feat(F-001)` incluye código + bitácora actualizada en el mismo commit.

## Checklist de calidad del spec (marcar antes del GATE C1)
- [x] Todo requisito es observable (no dice cómo implementarlo)
- [x] Tiene al menos un comportamiento de error (SI/THEN)
- [x] Cada requisito tiene un test o verificación asignada
- [x] Declara explícitamente qué queda fuera de alcance
