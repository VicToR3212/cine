from django.urls import path
# -------
from .views import crear_usuario,acceder,salir,sobre_nos
app_name = "apps.usuario"
urlpatterns = [
    path("Crear/", crear_usuario, name="crear_usuario"),
    path("Acceder/",acceder ,name='acceder'),
    path("Salir/",salir ,name='salir'),
    path("Sobre_Nosotros/",sobre_nos,name='Sobre_Nosotros'),
]
