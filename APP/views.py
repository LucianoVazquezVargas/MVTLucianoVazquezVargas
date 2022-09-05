from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familiares
def familiares(request):
    Pepe=Familiares(nombre="Pepe",DNI=45125556,telefono=144646516)
    Luciano=Familiares(nombre="Luciano",DNI=425846186,telefono=21156621)
    Juan=Familiares(nombre="Juan",DNI=564654103,telefono=215615416)
    Pepe.save()
    Luciano.save()
    Juan.save()
    diccionario={"Pepe":Pepe,"Luciano":Luciano,"Juan":Juan}
    plantilla=loader.get_template("template.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)