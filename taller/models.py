from django.db import models


class Taller(models.Model):
    """A mechanical workshop listed in the public catalog."""

    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    descripcion = models.TextField(blank=True)
    servicios = models.TextField(
        blank=True,
        help_text="Un servicio por línea (ej: frenos, suspensión, cambio de aceite).",
    )
    horario = models.CharField(max_length=200, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "talleres"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.ciudad})"
