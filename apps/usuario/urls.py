from django.urls import path
from django.views.generic import TemplateView
# -------
from .views import crear_usuario,acceder,salir,sobre_nos
app_name = "apps.usuario"
urlpatterns = [
    path("Crear/", crear_usuario, name="crear_usuario"),
    path("Acceder/",acceder ,name='acceder'),
    path("Salir/",salir ,name='salir'),
    path('Sobre_Nosotros/', TemplateView.as_view(template_name="Sobre_Nosotros.html"),name='Sobre_Nosotros'),
]
