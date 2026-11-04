from django.contrib import admin

from publicaciones.models import Publicacion

# Register your models here.



class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "fecha_creacion",
        "estado",
    )
    search_fields = (
        "titulo",
        "descripcion",
        "autor"
    )
    list_filter =(
        "estado",
        "fecha_creacion"
    )

admin.site.register(Publicacion,PublicacionAdmin)
admin.site.site_header = "Administracion de Glups"
admin.site.site_title = "Panel de Glups"
admin.site.index_title = "Gestion de publicaciones"