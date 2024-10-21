from django.db import models


class usuario(models.Model):
    pasword = models.CharField(max_length=30)
    nombreUser = models.CharField(max_length=30, blank=False)
    correo = models.EmailField(unique=True, max_length=50)
