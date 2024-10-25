from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout

from .forms import CrearpublicacionForm,Form_Modificacion
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import DeleteView, UpdateView
# ··------------------------------------------------------------
from .models import Publicacion,Comentario
from .forms import CrearpublicacionForm,Form_Modificacion,EdicionPublicacionForm

# ----
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.utils.dateformat import format





def is_colaborador(user):
    return user.groups.filter(name='moderador').exists()



# # -----------------------------   CREAR PUBLICACION-----------------

@login_required()
@user_passes_test(is_colaborador)
def crear_publicacion(request):
    form = CrearpublicacionForm()


    if request.method == "POST":
        form = CrearpublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = Publicacion()
            publicacion.nombre = form.cleaned_data["nombre"]
            publicacion.review = form.cleaned_data["review"]
            publicacion.enlace= form.cleaned_data["enlace"]
            publicacion.fechachaEmicion = form.cleaned_data["fechachaEmicion"]          
            publicacion.Categoria = form.cleaned_data["Categoria"]
            publicacion.imagen = form.cleaned_data["imagen"]
            publicacion.save()
            return redirect("apps.publicaciones:mostrarTodo_publicacion")
        else:
            print("invalido")
    contexto = {"form": form}
    return render(request, "publicar.html", {"form": form})


# -----------------------------   MOSTRAR TODOO PUBLICACION-----------------


def mostrarTodo_publicacion(request):
    return render(request, "portada.html", {"peliculas": Publicacion.objects.all()})


#--------------------------------   MOSTRAR PUBLICACION-----------------

@login_required()
def mostrar_publicacion(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    comentarios=Comentario.objects.all().filter(publicacion=publicacion)
    return render(request, "ver.html", {"publicacion": publicacion,"comentarios":comentarios})


# # -----------------------------   EDITAR PUBLICACION-----------------


def editar_publicacions(request, id): 
    # publicacion = get_object_or_404(Publicacion,id=id)     
    try:
        publicacion = Publicacion.objects.get(id=id)
    except Publicacion.DoesNotExist:
        return HttpResponse("publicacion no encontrada",status=404)

    if request.method == 'POST':
        form = EdicionPublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('apps.publicaciones:mostrarTodo_publicacion')  # Redirige a la lista de publicaciones o al detalle
    else:
        form = EdicionPublicacionForm(instance=publicacion)
        
    return render(request, "editar.html", {'form':form, 'publicacion':publicacion})
























def editar_publicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    fecha=format(publicacion.fechachaEmicion,'d-m-Y')
    form=CrearpublicacionForm(instance=publicacion)
    # form = CrearpublicacionForm(
    #     initial={
    #         "nombre": publicacion.nombre,
    #         "review": publicacion.review,
    #         "Categoria": publicacion.Categoria,
    #         "enlace": publicacion.enlace,
    #         "fechachaEmicion":fecha,
    #     }
    # )

    data = {"form": CrearpublicacionForm(request.POST)}
    if request.method == "POST":
        form = CrearpublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion.nombre = form.cleaned_data["nombre"]
            publicacion.review = form.cleaned_data["review"]
            publicacion.Categoria = form.cleaned_data["Categoria"]
            publicacion.imagen = form.cleaned_data["imagen"]
            publicacion.enlace = form.cleaned_data["enlace"]
            publicacion.fechachaEmicion = form.cleaned_data["fechachaEmicion"]
            publicacion.save()
            return redirect("apps.publicaciones:mostrarTodo_publicacion")
        else:
            print("invalido")
    contexto = {"form": form}
    return render(request, "publicar.html", {"form": form})


# # -----------------------------   eliminar PUBLICACION-----------------


@login_required()
@user_passes_test(is_colaborador)
def eliminar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    ima=publicacion.nombre
    ruta="media/"+str(publicacion.imagen)
    publicacion.delete()
    import os 
    os.remove(ruta)
    return redirect("apps.publicaciones:mostrarTodo_publicacion")

# #---------------------------FILTROS-----------------------------------

# #---------------------------filtros-----de la Z la  A------------------------------

def filtradoza(request):
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all().order_by('-nombre')})
# #---------------------------filtros  DE LA A la Z-----------------------------------

def filtradoaz(request):
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all().order_by('nombre')})

# #---------------------------filtros por fecha  mas mas antiguo al mas  moderno-----------------------------------

def filtradomenor(request):
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all().order_by('fechachaEmicion')})
# #---------------------------filtros por fecha  mas modeno al mas antiguo -----------------------------------

def filtradomayor(request):
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all().order_by('-fechachaEmicion')})



# -------------------------------------------------------------------------------------------------------------------------
#--------------------------------------COMENTARIOS---------------------------------------------------------------------------- 


def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Form_Modificacion()
        return context
    


#----------------------------------------------agregar---------------------------------------------------------------------------



def agregar_comentario(request,pk):
    publicacion=Publicacion.objects.get(id=pk)
    if request.method=="POST":
        form=Form_Modificacion(request.POST)
        if form.is_valid():
            
            comentario=form.save(commit=False)
            comentario.publicacion=publicacion
            
            comentario.usuario=request.user            
            
            comentario.save()
            return redirect("apps.publicaciones:mostrar_publicacion",pk=pk)
        else:

            return render (request,"ver.html",{"form":form,"publicacion":publicacion})
    else:
        return redirect("apps.publicaciones:mostrar_publicacion",pk=pk)
    

# -------------------------------MUESTRA LOS COMENTARIOS------------------------------------------------------------
def comentariosMostrar(request,pk):
    publicacion=Publicacion.objects.get(pk=pk)
    comentarios=Comentario.objects.filter(publicacion=publicacion)
    print(comentarios,"does")
    return render(request, "ver.html", {"comentarios":comentarios})



#-------------------------------BORRADO DE COMENTARIOS--------------------------------------------------------------
class BorrarComentario(DeleteView):
	model = Comentario
	def get_success_url(self):         
		return reverse_lazy('apps.publicaciones:mostrar_publicacion', kwargs={'pk': self.object.publicacion.pk})

#-------------------------------EDICION DE COMENTARIOS--------------------------------------------------------------
class ModificaComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'modificar.html'
	def get_success_url(self):         
		return reverse_lazy('apps.publicaciones:mostrar_publicacion', kwargs={'pk': self.object.publicacion.pk}) 

#Agregar Like al comentario
#Función add_like
@login_required
def add_like(request, pk, comentario_pk):
    # Obtener la publicación y el comentario
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentario = get_object_or_404(Comentario, pk=comentario_pk)

    # Verificar si el usuario ya ha dado "like"
    if request.user in comentario.likes.all():
        comentario.likes.remove(request.user)  # Quitar el "like"
    else:
        comentario.likes.add(request.user)  # Agregar el "like"
    return redirect ("apps.publicaciones:mostrar_publicacion",pk=pk)
     

        # 300mNsHyT