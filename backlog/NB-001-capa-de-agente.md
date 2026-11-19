- title:: Capa de agente — política de enrutamiento de modelos
- tipo:: [[necesidad]] · id:: NB-001 · estado:: aprobada
- fecha:: 2026-11-19 · fase:: 0 · origen:: propuesta de Daniel (revisión del pack, 2026-11-19) + feedback de Kevin

## Problema / necesidad
El dueño del producto programa con agentes y no puede revisar todo el código generado.
Hoy el pack no dice NADA sobre el agente que programa: qué modelo usar para qué tipo de
tarea. El riesgo concreto: un modelo gratuito alucina y el dueño (novato) no lo detecta.
La capa de más riesgo quedó sin rail.

## Criterio de éxito (medible)
- [ ] `docs/agentes.md` define niveles por TIPO DE TAREA sin nombres de modelo (la política no caduca).
- [ ] El guardián protege el documento nuevo y las plantillas actualizadas (check_pack PASS).
- [ ] Toda feature nueva registra el modelo usado por tarea (sección "Consumo del agente").

## Qué NO es
- No elige ni fija modelos concretos (eso vive en la config del agente, no en el repo).
- No instala herramientas ni cambia el stack.
- No cubre proyectos ML de SURA (ahí rigen las plantillas MLOps).

## Preguntas abiertas
- (ninguna — resueltas en la sesión de aprobación 2026-11-19)

## Historia
| fecha | de → a | motivo | quién |
|---|---|---|---|
| 2026-11-19 | nueva → aprobada | propuesta revisada y aprobada por Kevin con 2 ajustes | Kevin |
