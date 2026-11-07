# ADR-0003: protección del pack con guardián de integridad + hook pre-commit

- fecha:: 2026-11 · estado:: aceptada · decidida-por:: Kevin
- tipo:: proceso · origen:: riesgo real: agentes han borrado/reescribo archivos del pack

## Contexto
Los agentes tienen acceso de escritura total al working tree; las reglas (AGENTS.md)
son consejo, no puertas. Ya ha pasado que un agente borra o vacía los archivos de
contexto. Git permite recuperar, pero solo si alguien se da cuenta.

## Opciones consideradas
1. **Confiar en git history** — pro: cero trabajo. contra: solo detecta si alguien mira.
2. **Convención + chequeo manual en la sesión** — pro: simple. contra: depende de
   disciplina del agente (justo lo que falla).
3. **Guardián de integridad + hook pre-commit** — pro: puerta mecánica: el commit con
   daño se RECHAZA; el chequeo de estructura detecta el daño al iniciar la sesión.
   contra: script que mantener (pequeño, stdlib puro).

## Decisión
Opción 3. `ci/check_pack.py` (rutas requeridas, secciones requeridas, ADRs aceptados
inmutables por huella sha256 en `docs/decisions/INDEX.md`) + `.githooks/pre-commit`
activado con `git config core.hooksPath .githooks`.

## Consecuencias
- Modificar el pack (AGENTS.md, INICIO.md, docs/, _templates/) requiere actualizar el
  INDEX o aceptar el rechazo — y es una **escalación**, no una decisión del agente.
- Los ADRs aceptados son inmutables: un cambio nuevo = ADR nuevo que suplanta al anterior.
