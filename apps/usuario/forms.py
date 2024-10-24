from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import usuario
from django.contrib.auth.models import User


# aca se crea el formulario para registar usuarios
class CrearUsuarioForm(forms.Form):
   
    Username = forms.CharField(
        widget=forms.TextInput({"pleaceholder": "usuario", "class": "login_input"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "contraseña", "class": "login_input"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "contraseña", "class": "login_input"}
        )
    )

    class Meta:
        model = User
        # esta instrucion hace referencia a todos los atribuos
        fields = [ "username", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class logearForm(forms.ModelForm):
    usuario = forms.CharField(
        widget=forms.TextInput({"pleaceholder": "email", "class": "login_input"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "password", "class": "login_input"}
        )
    )

    class Meta:
        model = usuario
        # esta instrucion hace referencia a todos los atribuos
        fields = ["correo", "password1"]
        help_texts = {k: "" for k in fields}
