from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articulo, Categoria
from .forms import ArticuloForm 
# Create your views here.

#Aca se crea todo lo que es vista, se puede generar desde un archivo HTML o se
#Pueden usar los templates existentes en Django (ERRORES Y FORMularios de ingreso)
##########################################ARTICULOS########################################################

class PaginaPrincipal(ListView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/indexprueba.html'

class DetalleNoticia(DetailView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/paginanoticia.html'

class AgregarArticulo(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'SitioWebNoticiasCaos/creararticulo.html'

    #fields = ["tituloArticulo", "etiquetaTitulo", "contenidoArticulo", "sinopsisArticulo",
    #         "imagenArticulo", "usuarioAutor"]

class EditarArticulo(UpdateView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/editararticulo.html'
    fields = ["tituloArticulo", "etiquetaTitulo", "contenidoArticulo", "sinopsisArticulo", 'usuarioEditor', "imagenArticulo"]

class BorrarArticulo(DeleteView):
    model = Articulo 
    template_name = 'SitioWebNoticiasCaos/borrararticulo.html'
    success_url = reverse_lazy('indexprueba')

##########################################CATEGORIA########################################################

class AgregarCategoria(CreateView):
    model = Categoria
    template_name = 'SitioWebNoticiasCaos/creararticulo.html'
    fields ='__all__'





def contacto(request):
    return render(request, 'SitioWebNoticiasCaos/contacto.html')

def suscripcion(request):
    return render(request, 'SitioWebNoticiasCaos/suscripcion.html')

def login(request):
    return render(request, 'SitioWebNoticiasCaos/login.html')

def busqueda(request):
    return render(request, 'SitioWebNoticiasCaos/busqueda.html')

def contacto_laboral(request):
    return render(request, 'SitioWebNoticiasCaos/contacto_laboral.html')



def index(request):
    context={}
    return render(request, 'SitioWebNoticiasCaos/index.html', context)


