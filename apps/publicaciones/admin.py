from django.contrib import admin
from .models import Publicacion, Categoria,Comentario


admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)

# Register your models here.
# aca se agrega todos los models y se selecionas los datos a ver
