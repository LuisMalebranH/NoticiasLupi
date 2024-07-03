from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField 

# Create your models here.
class Categoria (models.Model):
    nombreCat = models.CharField(max_length=40, unique=True)
    

    def __str__(self):
        return str(self.nombreCat)

    def get_absolute_url(self):
        return reverse('indexprueba')




class Etiqueta (models.Model):
    nombreEtiqueta = models.CharField(max_length=40)

    def __str__(self):
    
        return str(self.nombreEtiqueta)


class Autor (models.Model):
    usuarioAutor = models.OneToOneField(User, on_delete=models.CASCADE)
    priNomAutor = models.CharField(max_length=15)
    segNomAutor = models.CharField(max_length=15) 
    apPaternoAutor = models.CharField(max_length=15) 
    apMaternoAutor = models.CharField(max_length=15) 
    # id_genero = ????
    fonoAutor = models.CharField(max_length=11)
    correoElectronico = models.CharField(max_length=40, default="example@email.com")

    def __str__(self):
        return str(self.usuarioAutor)

class Editor (models.Model):
    usuarioEditor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor')
    priNomEditor = models.CharField(max_length=15)
    segNomEditor = models.CharField(max_length=15) 
    apPaternoEditor = models.CharField(max_length=15) 
    apMaternoEditor = models.CharField(max_length=15) 
    # id_genero = ????
    fonoEditor = models.CharField(max_length=11)
    correoElectronico = models.CharField(max_length=40, default="example@email.com")

    def __str__(self):
        return str(self.usuarioEditor)

class Articulo (models.Model):
    
    tituloArticulo = models.CharField(max_length=255)
    etiquetaTitulo = models.CharField(max_length=255, default="Noticias Caos")
    contenidoArticulo = RichTextField(blank=True, null=True)
    #contenidoArticulo = models.TextField()
    sinopsisArticulo = models.CharField(max_length=255)
    imagenArticulo = models.ImageField(upload_to = "img/", blank=True, null=True)
    fechaPublicacion = models.DateField(auto_now_add=True)
    usuarioAutor = models.ForeignKey(Autor, related_name='articulos_autor', on_delete=models.CASCADE)
    usuarioEditor = models.ForeignKey(Editor, related_name='articulos_editor', on_delete=models.CASCADE, blank=True, null=True)
    nombreCat = models.CharField(max_length=255, default="Sin Asignar")


    def __str__(self):
        return self.tituloArticulo

    def get_absolute_url(self):
        return reverse('pagina_noticia', args=[str(self.pk)])




class PerfilUsuario (models.Model):
    usuarioPagina = models.OneToOneField(User, on_delete=models.CASCADE)
    nombrePerfil = models.CharField(max_length=40)

    def __str__(self):
        return str(self.nombrePerfil)
    # subscripcion =

    #Podriamos marcar la subscripcion como un booleano o podria ser una funcion que devuelva el estado de una subscripcion
    #activa usando un estado del tiempo, etonces solo actualizar el tiempo y dependiendo de
    # el dia genera el estado de sub

#class Comment(models.Model):
#    Articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comments')
#    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#    contenidoComentario = models.TextField()
#    horaPost = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return f'Comment by {self.user.username} on {self.article.title}'

