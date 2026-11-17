from django import forms

from .models import Autor, Publicacion


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
    
        fields = [
        "nombre",
        "apellido",
        "email",
        "avatar"
        
        ]

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
    
        fields = [
        "titulo",
        "descripcion",
        "autor",
        "estado",
        "imagen"
        ]

        widgets = {
        "descripcion" : forms.Textarea(
            attrs={"rows":5}
        )
        }