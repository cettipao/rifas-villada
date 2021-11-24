from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    cursos = [
        ("A", '7mo A'),
        ("B", '7mo B'),
        ("C", '7mo C'),
    ]
    curso = models.CharField(
        max_length=1,
        choices=cursos,
        blank=True,
        null = True
    )

    def __str__(self):
        return "{}".format(self.nombre)

    @property
    def rifas_vendidas(self):
        return len(Rifa.objects.filter(vendedor=self))

class Rifa(models.Model):
    comprador = models.CharField(max_length=30)
    vendedor = models.ForeignKey(
        'Vendedor',
        on_delete=models.CASCADE,
        null=False
    )
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} vendio a {}".format(self.vendedor, self.comprador)

