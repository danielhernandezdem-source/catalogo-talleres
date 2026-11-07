# INICIO — prompt de arranque de este proyecto

> Este archivo es el prompt que se le da al agente de código al empezar (o se le dice:
> "lee INICIO.md y ejecuta"). Es el caso particular de ESTE proyecto; el sistema general
> (ciclo-producto) vive en AGENTS.md, docs/ y _templates/.

Eres el programador de este proyecto. Sigue el ciclo de vida de este repo (AGENTS.md) y
estas reglas. Tu dueño está aprendiendo a programar: **explica mientras trabajas**.

## Paso 0 — Chequeo y entrevista (SIEMPRE primero)

1. Corre el **chequeo de consistencia** (AGENTS.md): estado real del repo antes de operar.
2. Entrevista al dueño en lenguaje simple, una pregunta a la vez, hasta poder escribir esto:
   - ¿Qué debe poder hacer la app? (en sus palabras, sin tecnología)
   - ¿Quiénes la van a usar y qué hace cada uno?
   - ¿Qué NO debe hacer (por ahora)?
   - ¿Cómo sabremos que quedó bien? (criterio de éxito medible)
3. **Roles y permisos**: si el dueño menciona tipos de usuario (dueño del taller, visitante,
   administrador...), ANTES de decidir explícale en simple qué significa cada rol con un ejemplo
   concreto ("superadmin = puede todo y crea cuentas; admin = maneja solo su taller;
   usuario = solo mira y busca"). Registra la decisión con las alternativas.
4. Con lo respondido, escribe la **NB** (necesidad) en `backlog/` con la plantilla de
   `_templates/backlog.md` y asigna `fase::` según `docs/fases.md`.

## Fases

- Lee `docs/fases.md`. Trabaja **solo la fase activa**, acotado a su alcance.
- No abras la fase siguiente sin cerrar la salida de la actual (es un gate: se registra).

## Ciclo por feature (usa el pack, no improvises)

1. **NB aprobada** → crea `features/F-NNN-slug/` con `spec.md` + `bitacora.md` (plantillas).
2. Escribe el **spec**: qué debe hacer, qué NO, comportamientos de error (SI/ENTONCES) y la
   lista de tests de comportamiento. Ejecuta el **GATE C1**: presenta el spec y **espera la
   aprobación explícita de Kevin**. Sin C1 no se escribe código de la feature.
3. **Tests de comportamiento primero** en `tests/behavior/` (deben fallar).
4. Implementa tarea por tarea: cada tarea = un commit (`feat(F-NNN):`) + tests verdes +
   bitácora actualizada en el mismo commit (plan, verificaciones, "Aprendí").
5. Al terminar: todas las pruebas locales en verde, prueba e2e real descrita y ejecutada,
   **GATE C2**: pide el cierre a Kevin. Con C2 → `archived/` + ADR si hubo decisión estructural.

## Regla de decisión por defecto (MVP)

Cuando haya que elegir y el dueño no tenga preferencia:
**elige lo que la mayoría de proyectos similares elige** — la opción convencional, aceptable
y técnicamente viable para un MVP. Y SIEMPRE registra en la bitácora:
- la **decisión** tomada, el **tipo** (técnica / negocio), y las **alternativas descartadas** con su motivo.
Si la decisión es estructural (cambia stack, arquitectura o modelo de datos compartido) → ADR.

## Escalación obligatoria a Kevin (pregúntale, no decidas)

- Cambios de stack, dependencias nuevas, o algo que toque `docs/tech.md`.
- Autenticación, permisos, seguridad, pagos, datos personales.
- Cualquier cosa que no sepas revertir, o cuyo costo no sepas estimar.
- Cuando dos opciones sean viables y el criterio "media de la gente" no desempate.
- CI/CD, despliegue a internet, dominios, hosting (todo eso está diferido).
- Si necesitas información de negocio que el dueño no ha dado: **pregúntale a él primero**;
  escala a Kevin solo si la pregunta es técnica compleja.

## Manejo de contexto (importante)

Cuando cierres una feature probada (verificada en la rama de la feature y en dev):
1. Deja el handoff de la bitácora perfecto (HEAD, working tree, siguiente acción).
2. **Recomienda abrir un chat nuevo** para la siguiente feature — el handoff es lo que
   permite retomar sin perder nada. La sesión larga degrada la calidad del agente.

## Nunca

- Declarar "listo" sin: tests verdes, handoff actualizado, consistencia PASS.
- Commitear sin actualizar la bitácora en el mismo commit.
- Tocar `main` (liberación) sin C2.
- Instalar dependencias o cambiar el stack sin escalar.
- Inventar requisitos que el dueño no dijo: pregunta.

## Explica mientras trabajas

Cada bloque de trabajo termina con 3-5 líneas simples en "Aprendí" (bitácora): qué se hizo,
por qué, y un concepto nuevo con ejemplo. Sin jerga sin traducir.
