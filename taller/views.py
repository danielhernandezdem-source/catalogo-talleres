from django.db.models import Q
from django.shortcuts import render

from .models import Taller


def home(request):
    """Public catalog home: list active workshops, optional text search."""
    query = request.GET.get("q", "").strip()
    talleres = Taller.objects.filter(activo=True)
    if query:
        talleres = talleres.filter(Q(nombre__icontains=query) | Q(ciudad__icontains=query))
    return render(request, "taller/index.html", {"talleres": talleres, "query": query})
