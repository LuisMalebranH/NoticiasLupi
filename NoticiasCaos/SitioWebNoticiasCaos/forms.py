from django import forms
from .models import Articulo, Categoria

from django.forms import ModelForm


QueryCategorias = Categoria.objects.all().values_list('nombreCat','nombreCat')

ListaCategorias = []

for item in QueryCategorias:
    ListaCategorias.append(item)

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = {'tituloArticulo', 
                    'sinopsisArticulo',
                    'contenidoArticulo',
                    'imagenArticulo',
                    'usuarioAutor'} 

        widgets = { 'tituloArticulo' : forms.TextInput(attrs={'class': 'form-control' }),
                    'sinopsisArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'contenidoArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'usuarioAutor': forms.Select(attrs={'class':'form-control'}),
                    }

# Arreglar form de Edicion despues
""" 
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = {'tituloArticulo', 
                    'contenidoArticulo', 
                    'sinopsisArticulo', 
                    'imagenArticulo',
                    'usuarioAutor'} 

        widgets = { 
                    'sinopsisArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'contenidoArticulo': forms.TextInput(attrs={'class': 'form-control' }), 
                    'tituloArticulo' : forms.TextInput(attrs={'class': 'form-control' }),
                    } 
    
"""