"""
URL configuration for glups_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from publicaciones import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name="base"),
    path('', views.inicio, name="inicio"),
    path("publicaciones/", views.lista_publicaciones, name="lista_publicaciones"),
    path("crear/",views.crear_publicacion,name="crear_publicacion"),
    path("editar/<int:id>",views.editar_publicacion,name="editar_publicacion"),
    path("eliminar/<int:id>",views.eliminar_publicacion,name="eliminar_publicacion"),
    path("autores/", views.lista_autores, name="lista_autores"),
    path("crear_autor/",views.crear_autor,name="crear_autor"),
    path("editar_autor/<int:id>",views.editar_autor,name="editar_autor"),
    path("contacto/", views.contacto, name="contacto")
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )