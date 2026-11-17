from django.db import models

# Create your models here.

class Publicacion (models.Model):
    ESTADOS = [("borrador","Borrador"),("publicado","Publicado"),("archivado", "Archivado")]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    #autor = models.ForeingKey(Autor,on_delete= models.CASCADE,related_name"publicaciones")
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default="borrador")
    imagen = models.ImageField(upload_to="publicaciones/",blank=True,null=True)
#FALTA RELACIONAR AUTOR CON EL MODELO AUTOR
    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        #return self.titulo
        return f"{self.titulo} - {self.autor}"
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to="avatars/",blank=True,null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    
    