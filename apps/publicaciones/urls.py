from django.urls import path
from .views import ModificaComentario,filtradoNenas,filtradoVarones,filtradoClasicos,BorrarComentario, agregar_comentario,filtradomayor,filtradomenor,filtradoza,filtradoaz,crear_publicacion,editar_publicacion,eliminar_publicacion,mostrar_publicacion, add_like
from django.views.generic import TemplateView
app_name = "apps.publicaciones"

urlpatterns = [
    # crear una publicacion. localhost:8000/publicaciones/crear/
    path("crear/", crear_publicacion, name="crear_publicacion"),
    # mostrar todas las pulicaciones
    # path("", mostrarTodo_publicacion, name="mostrarTodo_publicacion"),
    # mostrar una publicacion
    path("ver/<int:pk>", mostrar_publicacion, name="mostrar_publicacion"),
    # editar una publicacion
    path("editar/<int:id>", editar_publicacion, name="editar_publicacion"),
    # eliminar una publicacion
    path("eliminar/<int:id>", eliminar_publicacion, name="eliminar_publicacion"),
    path("filtradoaz/",filtradoaz, name="filtradoaz"),
    path("filtradoza/",filtradoza, name="filtradoza"),
    path("filtradomenor/",filtradomenor, name="filtradomenor"),
    path("filtradomayor/",filtradomayor, name="filtradomayor"),

    path("Nenas/",filtradoNenas, name="Nenas"),
    path("Varones/",filtradoVarones, name="Varones"),
    path("Clasico/",filtradoClasicos, name="Clasico"),

  	path("comentar/<int:pk>", agregar_comentario, name = "comentar"),
  	path('Borrar/<int:pk>', BorrarComentario.as_view(), name="borrar_comentario"),
  	path('Modificar/<int:pk>', ModificaComentario.as_view(), name="modificar_comentario"),
    path('comentar/<int:pk>/like/<int:comentario_pk>', add_like, name='like'),
    path('Contacto/', TemplateView.as_view(template_name="contacto.html"),name='Contacto'),

]