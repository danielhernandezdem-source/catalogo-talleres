"""Behavior tests for the public catalog (Fase 0 smoke)."""

import pytest
from django.urls import reverse

from taller.models import Taller

pytestmark = pytest.mark.django_db


def test_home_lists_active_workshops_only(client):
    Taller.objects.create(nombre="Taller Chepe", ciudad="Piedecuesta")
    Taller.objects.create(nombre="Motos RC", ciudad="Bucaramanga", activo=False)

    response = client.get(reverse("home"))

    assert response.status_code == 200
    html = response.content.decode()
    assert "Taller Chepe" in html
    assert "Motos RC" not in html  # inactive workshops are hidden


def test_home_search_filters_by_name(client):
    Taller.objects.create(nombre="Taller Chepe", ciudad="Piedecuesta")
    Taller.objects.create(nombre="Frenos del Valle", ciudad="Bucaramanga")

    response = client.get(reverse("home"), {"q": "chepe"})

    html = response.content.decode()
    assert "Taller Chepe" in html
    assert "Frenos del Valle" not in html
