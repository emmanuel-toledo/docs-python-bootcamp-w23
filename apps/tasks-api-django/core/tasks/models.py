from django.db import models

# Create your models here.

# Necesario heredar de Model para llevar a cabo la migración.
class Task(models.Model):
    # Definimos el tipo de dato de la columna que tendrá en la base de datos.
    title = models.CharField(max_length=200)
    # Definimos columna tipo Boolean
    # is_completed = models.BooleanField(default = False)

    # Representación del módelo en string.
    def __str__(self) -> str:
        return f"ID: {self.pk} - {self.title}"