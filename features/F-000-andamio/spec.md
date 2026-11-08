# Spec: andamio del proyecto (F-000)

- origen:: decisión de arranque (Kevin) · estado:: verificada-e2e
- fecha:: 2026-11 · aprobada-por:: Kevin (GATE C1: aprueba su propio andamio)

## Qué debe hacer
El repo debe permitir, desde un clon fresco y sin pasos ocultos:
1. Instalar y correr la app en local (`runserver`) con la página de inicio visible.
2. Correr los gates físicos: tests, lint y checks de Django, todos en verde.
3. Administrar talleres desde el admin de Django.

## Qué NO debe hacer
- No hay despliegue a internet ni CI en la nube (ADR-0002).
- No hay Node/npm ni Docker (ADR-0001).

## Comportamientos de error
- SI la base de datos no existe, ENTONCES `migrate` la crea sin pasos manuales.
- SI un taller está `activo=False`, ENTONCES no aparece en el listado público.
- SI la búsqueda no encuentra nada, ENTONCES la página muestra un mensaje claro
  (no una página rota ni un listado vacío sin explicación).

## Verificación end-to-end (esta es la prueba que debe pasar todo programador)
| id | comportamiento | cómo se verifica | resultado |
|---|---|---|---|
| T1 | Un clon fresco instala, migra, corre tests y lint | clone → `uv venv` → `uv pip install -r requirements.txt` → `migrate` → `pytest` → `ruff check` | ✅ 2/2 tests, ruff limpio |
| T2 | La app enciende y muestra el catálogo | `runserver` + navegador en `http://127.0.0.1:8000` | ✅ HTTP 200, título visible |
| T3 | El listado oculta talleres inactivos y filtra por búsqueda | `pytest` (2 tests de `tests/behavior/`) | ✅ |
| T4 | El admin permite administrar talleres | `/admin/` con el superusuario | ✅ HTTP 200 |

## Checklist de calidad del spec
- [x] Todo requisito es observable
- [x] Tiene comportamientos de error (SI/THEN)
- [x] Cada requisito tiene verificación asignada
- [x] Declara qué queda fuera de alcance
