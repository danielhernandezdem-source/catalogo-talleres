# Agentes de código y modelos — política de enrutamiento

- estado:: v1 · fecha:: 2026-11 · decidida-por:: Kevin
- tipo:: proceso · origen:: revisión del pack (catálogo de talleres) · ver [[NB-001]]

## Quién programa
El dueño del producto programa con asistencia de agentes. El agente ejecuta; el humano
aprueba. La selección de modelo es parte del proceso, no una preferencia del agente.

## Regla de oro
El modelo se elige por **tipo de tarea**, no por fase ni por preferencia del agente.
El nivel lo declara la tarea; el humano puede subirlo; el agente lo registra.

**Separación de capas**: este repo define la POLÍTICA (niveles por tipo de tarea, sin
nombres de modelo). La config del agente define la RUTA (el modelo concreto de hoy).
La skill define el PROCEDIMIENTO (cómo cambiar y cómo registrar). Así este documento
no caduca cuando un modelo concreto desaparece del catálogo.

## Niveles
| nivel | cuándo | por qué |
|---|---|---|
| FUERTE | entender requerimiento, spec ambiguo, plan de arquitectura, ADR, revisar diff, decidir un enfoque | un error aquí cuesta días |
| ILIMITADO | código repetitivo, tests, renombrados, formateo, leer archivos, títulos, resúmenes, bitácora | volumen, no criterio |
| NUNCA SOLO | cualquier cosa que el dueño no pueda verificar | un modelo gratuito alucina y el dueño (novato) no lo detecta |

`NUNCA SOLO` opera como los gates conceptuales (C1/C2): la tarea no se cierra sin
verificación humana **registrada por nombre y fecha** en la bitácora (sección
"Registro de verificaciones"). Sin esa fila, no está hecha.

## Escalación de modelo
- Una tarea ILIMITADO que falla dos veces seguidas → sube a FUERTE y se registra en la bitácora.
- Si el dueño no entiende una explicación → sube a FUERTE.
- Si el agente no sabe estimar el costo o no sabe revertir algo → escala a Kevin
  (ver "Escalación obligatoria a Kevin" en INICIO.md).

## Registro
Cada feature anota en su bitácora (sección "Consumo del agente") el nivel y el modelo
concreto usado por tarea, junto con las cuotas del proveedor de ese día. Es **evidencia
viva**: caduca y se actualiza sin escalación. La política estable vive aquí.

## Consecuencias
- Las tareas ILIMITADO se ejecutan sin fricción; las FUERTE exigen que el agente declare
  el nivel antes de empezar.
- `NUNCA SOLO` es la regla que protege al dueño: sin verificación humana registrada no
  se cierra nada.
- Cambiar este documento es una escalación (el guardián lo protege).
