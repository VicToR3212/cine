from django.urls import path
from .views import crear_usuario,acceder,salir,Sobre_Nosotros

app_name = "apps.usuario"

urlpatterns = [
    path("Crear/", crear_usuario, name="crear_usuario"),
    path("Acceder/",acceder ,name='acceder'),
    path("Salir/",salir ,name='salir'),
    path("Sobre_Nosotros/",Sobre_Nosotros,name='Sobre_Nosotros'),
]
