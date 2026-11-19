- title:: F-001-capa-de-agente — bitácora
- tipo:: [[bitacora-feature]] · feature:: F-001 · estado:: en-ejecucion
- origen:: [[NB-001]] · rama:: feature/F-001-capa-de-agente · ambiente:: dev (local)
- head:: b43cff4 · actualizado:: 2026-11-19

## Historia del ciclo
| fecha | de → a | evidencia | gate |
|---|---|---|---|
| 2026-11-19 | borrador → en-ejecucion | spec aprobado por Kevin en sesión 2026-11-19 (propuesta de Daniel + 2 ajustes de Kevin: cuotas a la bitácora, NUNCA SOLO con evidencia) | C1 |

## Plan (bloques ejecutables)
1. ✅ Fixes H1/H2 (guardián en clones frescos + texto de plantillas) — commit `b43cff4`
2. ⬜ `docs/agentes.md` (política, sin modelos ni cuotas) + ADR-0004 + INDEX
3. ⬜ Plantillas: bitácora "Consumo del agente" + spec "Modo de modelo por bloque"
4. ⬜ `docs/metricas.md`: M6 coste del agente, M7 deriva de modelo
5. ⬜ Guardián: proteger `docs/agentes.md` (REQUIRED_PATHS + REQUIRED_SECTIONS)
6. ⬜ Verificación T1-T4 + e2e → GATE C2

## Registro de verificaciones
| fecha | tipo | qué corrió | ambiente | resultado | evidencia | aprobó |
|---|---|---|---|---|---|---|
| 2026-11-19 | gate F (local) | `uv run python ci/check_pack.py` | dev | PASS | commit b43cff4 (falló con hooksPath=vacio, pasó con .githooks) | — |

## Consumo del agente
| fecha | tarea | nivel | modelo usado | notas |
|---|---|---|---|---|
| 2026-11-19 | escritura del spec + fixes del pack | FUERTE | z-ai/glm-5.3-flash (Hermes, sesión Kevin) | cuotas del día: OpenRouter free 20 req/min, 50 req/día (1000/día con $10 una vez); Nous free 50 req/min, 500K tokens/min. EVIDENCIA — caduca, no es política |

## Decisiones tomadas durante la feature
- (2026-11-19) Separación REPO=política / CONFIG=ruta / SKILL=procedimiento — tipo: proceso.
  Alternativas descartadas: fijar modelos en docs/agentes.md (caduca dentro de un doc
  protegido → cada cambio sería escalación); no documentar nada (H3: riesgo sin rail).
- (2026-11-19) Cuotas de proveedores como evidencia en bitácora, no en docs/agentes.md —
  tipo: proceso. Alternativa descartada: cuotas en el doc protegido (se pudren y el
  guardián las vuelve caras de actualizar).

## Aprendí (explicaciones para el dueño)
- **Política vs ruta**: el repo dice "qué tipo de tarea merece qué nivel de modelo" (eso
  casi nunca cambia); tu config del agente dice "hoy uso el modelo X" (eso cambia cada
  mes). Igual que una constitución vs un horario: si los mezclas, cada cambio pequeño
  obliga a editar la constitución.
- **NUNCA SOLO**: significa que esa tarea no se cierra sin que un humano la verifique y
  quede registrado quién y cuándo. Es el mismo mecanismo de los gates conceptuales
  (C1/C2) que ya existen: evidencia con nombre y fecha, no buena voluntad.

## Commits
- `b43cff4` fix(pack): guardián visible y activo en clones frescos

## Lecciones (→ reusar en el proyecto)
- `core.hooksPath` no viaja con git: documentar su activación como paso 0 de clon nuevo.

## Handoff (contexto mínimo viable)
- HEAD: `b43cff4` · working tree: sucio (NB-001 + spec + esta bitácora sin commit)
- Estado: GATE C1 registrado; falta implementar bloques 2-6.
- Siguiente acción: docs/agentes.md + ADR-0004 + plantillas + guardián, luego verificación T1-T4 y GATE C2 con Kevin.
