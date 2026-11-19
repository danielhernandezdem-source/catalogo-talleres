# Spec: <feature> (F-<NNN>)

- origen:: [[NB-<NNN>]] · estado:: borrador
- fecha:: <AAAA-MM-DD> · aprobada-por:: — (GATE C1 pendiente)

## Qué debe hacer
<comportamiento observable, no implementación. "el sistema debe", no "usamos Redis">

## Qué NO debe hacer (fuera de alcance)
- <exclusiones explícitas — la mitad que evita defectos>

## Comportamientos de error (obligatorios)
- SI <falla X>, ENTONCES el sistema debe <respuesta determinista>
- (un spec sin líneas SI/THEN está incompleto)

## Tests de comportamiento (se escriben ANTES de codificar)
| id | comportamiento | cómo se verifica |
|---|---|---|
| T1 | <comportamiento> | test de `tests/behavior/` |
| T2 | <comportamiento> | prueba manual con pasos concretos |

## Modo de modelo por bloque
| bloque del plan | nivel (docs/agentes.md) | justificación |
|---|---|---|
| | | |

(La política de niveles vive en `docs/agentes.md`; el modelo concreto lo pone la config
del agente y se registra en la bitácora. Declarar el nivel es obligatorio antes de
ejecutar tareas FUERTE.)

## Verificación end-to-end (paso final del spec)
<los pasos concretos que prueban que la feature funciona de punta a punta>

## Declaración del GATE C2 (completa antes de pedirlo)
- qué aprueba:: <transición exacta; si aprueba merge: rama origen → rama destino>
- comportamientos esperados:: <qué debe poder hacer el sistema tras el cambio>
- NO afectado (regresión):: <comportamientos previos intactos + evidencia>
- evidencia:: <tests/chequeos con su resultado exacto>
- si se rechaza:: <qué se rehace o restaura>
(Sin estos cinco campos el gate no se presenta: el humano no puede decidir a ciegas.)

## Checklist de calidad del spec (marcar antes del GATE C1)
- [ ] Todo requisito es observable (no dice cómo implementarlo)
- [ ] Tiene al menos un comportamiento de error (SI/THEN)
- [ ] Cada requisito tiene un test o verificación asignada
- [ ] Declara explícitamente qué queda fuera de alcance
