
from django.shortcuts import render
from apps.publicaciones.models import Publicacion


def inicio(request):  
    peliculas=Publicacion.objects.all()
    return render(request, "portada.html", {"peliculas": peliculas})

def ejemplo():
    pass