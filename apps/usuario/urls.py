from django.urls import path
from .views import crear_usuario,acceder,salir

app_name = "apps.usuario"

urlpatterns = [
    path("crear/", crear_usuario, name="crear_usuario"),
    path("acceder/",acceder ,name='acceder'),
    path("salir/",salir ,name='salir'),

   

]
