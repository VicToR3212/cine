from django.shortcuts import render, get_object_or_404, redirect
from .forms import CrearpublicacionForm,Form_Modificacion, CajaComentario
from .models import Publicacion,Comentario
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import DeleteView, UpdateView
from django.views import View
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse


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


# # -----------------------------   MOSTRAR PUBLICACION-----------------

@login_required()
def mostrar_publicacion(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    Agregar_Comentario(request,pk)
    print("mmmmmmmmmmmmm")
    return render(request, "ver.html", {"publicacion": publicacion})


# # -----------------------------   EDITAR PUBLICACION-----------------

@login_required()
@user_passes_test(is_colaborador)
def editar_publicacion(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    form = CrearpublicacionForm(
        initial={
            "nombre": publicacion.nombre,
            "review": publicacion.review,
            "Categoria": publicacion.Categoria,
            "enlace": publicacion.enlace,
            "fechachaEmicion":publicacion.fechachaEmicion
        }
        
    )

    
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

# #---------------------------filtros-----------------------------------

# #---------------------------filtros-----de la Z la  A------------------------------

def filtradoza(request):
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all().order_by('-nombre')})
    #filtradomayot,filtradomenor,filtradoza,filtradoaz
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
# comentarioss 


# ver comentario 

# class Postdetalleview(generic.DetailView):
#     model=Comentario
#     queryset = Comentario.objects.filter(
#         pub_date_lte=timezone.now()
#     )

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Form_Modificacion()
        return context
    



#--------agregar



def Agregar_Comentario(request,pk):
    form=Form_Modificacion(request.POST)
    print("donde estoy 1")

    publicacion=Publicacion.objects.get(pk=pk)
    print(publicacion ,"es la publi ")

    comentarios=Comentario.objects.filter(publicacion=publicacion)
    print(comentarios)
    if request.method=='POST':
        print("donde estoy")
        form=Form_Modificacion(request.POST)
        if form.is_valid():
            print("save")
            comentario=form.save(commit=False)
            comentario.publicacion=publicacion
            comentario.usuario=request.user            
            comentario.save()
            return redirect("ver.html",pk=pk)
        else:
            form=Form_Modificacion()
        return render(request,"ver.html",{'comentarios':comentarios,"form":form})

#borrar
class BorrarComentario(DeleteView):
	model = Comentario
	def get_success_url(self):         
		return reverse_lazy('publicaciones:detalle_publicacion',kwargs={'pk': self.object.publicacion.pk})

# modificar
class ModificaComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'ver.html'
	def get_success_url(self):         
		return reverse_lazy('publicaciones:detalle_publicacion',kwargs={'pk': self.object.publicacion.pk})

#Agregar Like al comentario
@login_required
class AddLike(View):
     def post (self, request, pk, *args, **kwargs):
          publicacion=Publicacion.objects.get(pk=pk)

          is_like = False
          for like in Comentario.likes.all():
               if like == request.user:
                    is_like = True
                    break
          if not is_like:
               Comentario.likes.add(request.user)
          if is_like:
               Comentario.likes.remove(request.user) 

          next = request.POST.get('next', '/')
          return HttpResponseRedirect(next)
     


        # 300mNsHyT