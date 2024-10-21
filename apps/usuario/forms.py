from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import usuario


# aca se crea el formulario para registar usuarios
class CrearUsuarioForm(forms.Form):
    correo = forms.EmailField(
        widget=forms.TextInput(attrs={"pleaceholder": "coreo", "class": "login_input"})
    )
    nombreUser = forms.CharField(
        widget=forms.TextInput({"pleaceholder": "usuario", "class": "login_input"})
    )
    pasword = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "contraseña", "class": "login_input"}
        )
    )
    pasword2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "contraseña", "class": "login_input"}
        )
    )

    class Meta:
        model = usuario
        # esta instrucion hace referencia a todos los atribuos
        fields = ["correo", "nombreUser", "pasword", "pasword2"]
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
