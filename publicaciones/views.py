from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .forms import AutorForm, PublicacionForm
from .models import Autor, Publicacion

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
    autores = Autor.objects.all()
    contexto = {"autores": autores}
    return render(request, "publicaciones/lista_autores.html", contexto)

# ---------------
# CREATE
# ---------------

def crear_publicacion(request):
    if request.method == "POST":
        formulario = PublicacionForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_publicaciones")
    else:
        formulario = PublicacionForm()
    return render(request,"publicaciones/crear_publicacion.html",{"formulario":formulario})

def crear_autor(request):
    if request.method == "POST":
        formulario = AutorForm(
            request.POST,
            request.FILES
        )
        if formulario.is_valid():
            formulario.save()
            return redirect("lista_autores")
    else:
        formulario = AutorForm()
    
    return render(request,"publicaciones/crear_autor.html",{"formulario":formulario})
    

# ---------------
# UPDATE
# ---------------
def editar_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)

    if request.method == "POST":
        formulario = PublicacionForm(
            request.POST,
            request.FILES,
            instance=publicacion
        )

        if formulario.is_valid():

            publicacion.save()

            return redirect("lista_publicaciones")
    else:
        formulario = PublicacionForm(instance=publicacion)
    return render(request,"publicaciones/editar_publicacion.html",{"publicacion":publicacion,"formulario":formulario})

#Proximamente editamos esto y es def editar_perfil
def editar_autor(request,id):
    autor = get_object_or_404(Autor,id=id)
    if request.method == "POST":
        formulario = AutorForm(
            request.POST,
            request.FILES,
            instance=autor
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_autores")
    else:
        formulario = AutorForm(instance=autor)
    
    return render(request,"publicaciones/editar_autor.html",{"autor":autor,"formulario":formulario})

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