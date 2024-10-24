from django.shortcuts import redirect

def logout_required(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect("apps.publicaciones:mostrarTodo_publicacion")
        return view(request)

    return wrapper 