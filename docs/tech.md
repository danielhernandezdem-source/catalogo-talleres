# Stack — decisiones técnicas del proyecto

- estado:: v1 · fecha:: 2026-11 · decisiones en: `docs/decisions/`

## Stack aprobado

| Capa | Elección | Versión |
|---|---|---|
| Lenguaje | Python | 3.12 (venv con uv) |
| Backend | **Django LTS** | 5.2.x |
| Frontend | Django templates + HTMX + Bootstrap 5 (CDN) | — |
| Base de datos | **SQLite** (archivo local `db.sqlite3`) | la que trae Python |
| Tests | pytest + pytest-django | latest |
| Lint | ruff | latest |
| CI/CD | **diferido** (ver debates) | — |

## Por qué (resumen)

- Máquina modesta (dual core, 3 GB RAM, Lubuntu LTS): sin Node/npm, sin Docker, sin builds de JS.
- Django da gratis: ORM + migraciones + admin panel (el CRUD del catálogo) + auth.
- SQLite: cero servidor que instalar; el ORM de Django es el desacople para migrar después a Postgres.
- HTMX: interactividad sin build de JavaScript.

## Migración futura (cuando haya éxito)

Postgres: cambiar el engine en `settings.py`, instalar `psycopg`, correr migraciones con los
datos en un dump. Nada del código de la app cambia: esa es la razón de esta elección.

## Prohibiciones (hasta nueva decisión escalada)

- Node/npm (y todo lo que requiera build de JS).
- Docker, contenedores, orquestadores.
- Servicios en la nube, hosting, dominios.
- Credenciales o secretos en el código.
