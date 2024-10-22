from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# --------------------crearusuario----------------------------------------------------------------
def crear_usuario(request):
    if request.method == "GET":

        return render(request, "registration/registrarce.html",{"form": UserCreationForm})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "registration/registrarce.html",{"form": UserCreationForm,'error':"contraseñas no coinciden"})
        else:
            
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, "registration/registrarce.html",{"form": UserCreationForm,'error':"usuario ya existente"})
                
            else:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect("apps.publicaciones:mostrarTodo_publicacion")
                

        




# ---------------------------------------cerrar sesion---------------------------------------------------------------


def salir (request):
    logout(request)
    return redirect('/')


# -----------------iniciar sesion  de usuario ------------------------------------------------------------------

def acceder(request):
    if request.method=='GET':
        return render(request,"registration/login.html",{"form":AuthenticationForm})

    else:
        user=authenticate(username=request.POST[ 'username'],password=request.POST['password'])
        if user is None:
            return render(request,"registration/login.html",{"form":AuthenticationForm ,'error':"contraseñas o usuariio no coinciden"})
        else:
            login(request,user)
            return redirect("apps.publicaciones:mostrarTodo_publicacion")
            


# ------------------------------------------------------------------------------------------------------
