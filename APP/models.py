from django.db import models

class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    DNI=models.IntegerField()
    telefono=models.IntegerField()