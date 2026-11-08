# CI/CD — DIFERIDO (ver docs/decisions/ADR-0002-ci-diferido.md y docs/debates.md D-001)

# Cuando se active, este workflow correrá lo mismo que corren los gates físicos locales:
#   - uv run ruff check .
#   - uv run pytest
#   - uv run python manage.py check --deploy (solo al liberar)
# No activar sin decisión registrada (escalación a Kevin).
