from django.contrib import admin

from .models import Taller


@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "telefono", "activo")
    list_filter = ("ciudad", "activo")
    search_fields = ("nombre", "ciudad", "descripcion", "servicios")
