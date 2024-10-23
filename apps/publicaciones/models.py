from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth import get_user_model
User = get_user_model()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    nombre = models.CharField(max_length=30)
    review = models.CharField(max_length=300)
    enlace = models.CharField(max_length=500,null=False)
    fechachaEmicion = models.DateField(default=now,null=False)
    Categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="publicaciones/", blank=True, null=True)

    def __str__(self):
        return self.nombre
# DateField:



# ---------comentarios


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')


    
    def __str__(self):

        return self.texto