# ADR-0004: capa de agente — política de enrutamiento de modelos separada de la ruta

- fecha:: 2026-11-19 · estado:: aceptada · decidida-por:: Kevin
- tipo:: proceso · origen:: propuesta de Daniel (H3) + [[NB-001]]

## Contexto
El pack no decía nada sobre el agente que programa: ni modelo, ni nivel, ni costo.
Para el caso de uso real —el dueño programa con experiencia nula— eso dejaba sin rail
justo el riesgo mayor: que un modelo gratuito alucine código que el dueño no puede
verificar. Además, un documento de proceso que nombre modelos concretos caduca en cuanto
el proveedor cambia el catálogo o las cuotas.

## Opciones consideradas
1. **No documentar nada** — pro: cero ceremonia. contra: el riesgo H3 queda sin rail.
2. **Fijar modelos y cuotas en un doc del repo** — pro: todo en un lugar. contra: caduca
   (cuotas y catálogos cambian) y al estar protegido por el guardián, cada actualización
   sería una escalación.
3. **Separar política (repo) / ruta (config del agente) / procedimiento (skill)** —
   pro: la política es estable y no caduca; la evidencia viva (modelo usado, cuotas del
   día) va a la bitácora de cada feature, donde actualizarla es barato. contra: dos
   lugares que mantener (pero uno casi no cambia).

## Decisión
Opción 3. `docs/agentes.md` (protegido por el guardián) define niveles por TIPO DE TAREA
— FUERTE / ILIMITADO / NUNCA SOLO — sin nombres de modelo. Los nombres y las cuotas viven
en la config del agente y en la sección "Consumo del agente" de cada bitácora
(evidencia). `NUNCA SOLO` opera con el mismo mecanismo de los gates conceptuales:
verificación humana registrada por nombre y fecha.

## Consecuencias
- El documento no caduca cuando desaparece un modelo `:free`.
- Registrar el consumo por tarea es obligatorio desde hoy (M6/M7 en `docs/metricas.md`
  lo miden).
- Modificar `docs/agentes.md` es una escalación, como el resto del pack.
