from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from publicaciones.models import Publicacion

# Create your views here.
def base(request):
    return render (request, "publicaciones/base.html")

def inicio(request):
    return render(request, "publicaciones/inicio.html")
# ---------------
# READ
# ---------------
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    contexto = {"publicaciones": publicaciones }
    return render(request, "publicaciones/lista_publicaciones.html", contexto)

# Falta modificar esto
def lista_autores(request):
    autores = [
        {"nombre":"Camila", "post": 3},
        {"nombre":"Evelyn", "post": 5},
        {"nombre":"Pedro", "post": 2}
        ]
    contexto = {"autores": autores}
    return render(request, "publicaciones/lista_autores.html", contexto)

# ---------------
# CREATE
# ---------------

def crear_publicacion(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        autor = request.POST["autor"]
        estado = request.POST["estado"]
        Publicacion.objects.create(
            titulo = titulo,
            descripcion = descripcion,
            autor = autor,
            estado = estado
        )
        return redirect("lista_publicaciones")
    return render(request,"publicaciones/crear_publicacion.html")

# ---------------
# UPDATE
# ---------------
def editar_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)

    if request.method == "POST":
        publicacion.titulo = request.POST["titulo"]
        publicacion.descripcion = request.POST["descripcion"]
        publicacion.autor = request.POST["autor"]
        publicacion.estado = request.POST["estado"]

        publicacion.save()

        return redirect("lista_publicaciones")
    return render(request,"publicaciones/editar_publicacion.html",{"publicacion":publicacion})

# ---------------
# DELETE
# ---------------

def eliminar_publicacion(request,id):
    publicacion= get_object_or_404(Publicacion,id=id)
    if request.method == "POST":
        publicacion.delete()
    
    return redirect("lista_publicaciones")


def contacto(request):
    return render (request, "publicaciones/contacto.html")

#SELECT * FROM Publicacion
#Publicacion.objects.all()
#Publicacion.objects.filter(estado="publicado")
#Publicacion.objects.get(id=1) --> get_object_or_404()

#publicaciones = Publicacion.objects.all()