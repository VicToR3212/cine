# ACA SE VA CREAR UN FORMULARIO BASADO A LOS DATOS QUE SE DESEAN EN EL FORMULARIO
from django import forms
# -----------------------
from .models import Publicacion, Categoria,Comentario


class CrearpublicacionForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    review = forms.CharField(widget=forms.TextInput())
    enlace = forms.CharField(widget=forms.TextInput())   
    fechachaEmicion = forms.CharField( widget=forms.DateInput(attrs= {'type':"date",}))
    Categoria= forms.ModelChoiceField(
        label="categoria", queryset=Categoria.objects.all()
    )
    imagen = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Publicacion
        # esta instrucion hace referencia a todos los atribuos
        fields = ["nombre", "review", "enlace", "fechachaEmicion","Categoria","imagen"]
        help_texts = {k: "" for k in fields}

# ---------------------editpublic
class EdicionPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ["nombre", "review", "enlace", "fechachaEmicion","Categoria","imagen"]


# --------------------------COEMNTARIOS----------------------------





class Form_Modificacion(forms.ModelForm):


    class Meta:
        model = Comentario
        fields = ('texto',)