- title:: F-001-capa-de-agente — bitácora
- tipo:: [[bitacora-feature]] · feature:: F-001 · estado:: completada
- origen:: [[NB-001]] · rama:: feature/F-001-capa-de-agente · ambiente:: dev (local)
- head:: fdc7abf · actualizado:: 2026-11-19

## Historia del ciclo
| fecha | de → a | evidencia | gate |
|---|---|---|---|
| 2026-11-19 | borrador → en-ejecucion | spec aprobado por Kevin en sesión 2026-11-19 (propuesta de Daniel + 2 ajustes de Kevin: cuotas a la bitácora, NUNCA SOLO con evidencia) | C1 |
| 2026-11-19 | en-ejecucion → verificada-e2e | T1-T4 + pytest 2 passed + PACK: OK (tabla de abajo) | F (evidencia) |
| 2026-11-19 | verificada-e2e → completada + merge a main | aprobación con declaración completa (spec §Declaración GATE C2); Kevin aprueba apoyado en la evidencia registrada, sin re-verificación manual propia — registrada tal cual | C2 |

## Plan (bloques ejecutables)
1. ✅ Fixes H1/H2 (guardián en clones frescos + texto de plantillas) — commit `b43cff4`
2. ✅ `docs/agentes.md` (política, sin modelos ni cuotas) + ADR-0004 + INDEX
3. ✅ Plantillas: bitácora "Consumo del agente" + spec "Modo de modelo por bloque"
4. ✅ `docs/metricas.md`: M6 coste del agente, M7 deriva de modelo
5. ✅ Guardián: proteger `docs/agentes.md` (REQUIRED_PATHS + REQUIRED_SECTIONS)
6. ✅ Verificación T1-T4 → pendiente GATE C2

## Registro de verificaciones
| fecha | tipo | qué corrió | ambiente | resultado | evidencia | aprobó |
|---|---|---|---|---|---|---|
| 2026-11-19 | gate F (local) | `uv run python ci/check_pack.py` | dev | PASS | commit b43cff4 (falló con hooksPath=vacio, pasó con .githooks) | — |
| 2026-11-19 | verificación T1 | check_pack con `docs/agentes.md` movido fuera → falla `FALTA` → restaurado → PASS | dev | PASS 2/2 | ejecución en sesión 2026-11-19 | — |
| 2026-11-19 | verificación T1b | check_pack con sección `## Registro` eliminada del doc → falla `SECCIÓN FALTANTE` → restaurado → PASS | dev | PASS | ejecución en sesión 2026-11-19 | — |
| 2026-11-19 | verificación T2 | `grep -icE "openrouter\|nous\|gpt\|claude\|gemini\|glm" docs/agentes.md` | dev | 0 coincidencias | ejecución en sesión 2026-11-19 | — |
| 2026-11-19 | verificación T3 | `check_pack.py --update-index` → 4 ADRs registrados; huella ADR-0004 en INDEX; check PASS | dev | PASS | docs/decisions/INDEX.md | — |
| 2026-11-19 | verificación T4 | check_pack valida secciones nuevas de plantillas (`Consumo del agente`, `Modo de modelo por bloque`) | dev | PASS | REQUIRED_SECTIONS actualizado + PACK: OK | — |

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
- `fdc7abf` gate(F-001): NB-001 aprobada + spec C1 → en-ejecucion
- (este commit) feat(F-001): capa de agente — política, ADR-0004, plantillas, métricas M6/M7, guardián

## Lecciones (→ reusar en el proyecto)
- `core.hooksPath` no viaja con git: documentar su activación como paso 0 de clon nuevo.

## Handoff (contexto mínimo viable)
- HEAD: `a10952e` (rama) · working tree: limpio tras commit de cierre
- Estado: F-001 COMPLETADA con C2 de Kevin (2026-11-19); merge a main y push hechos.
- Siguiente acción: ninguna de esta feature. Para el dueño: en su clon, correr
  `git pull` + `git config core.hooksPath .githooks` (paso 0 de INICIO.md).
