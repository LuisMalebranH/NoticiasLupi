#from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import PaginaPrincipal, DetalleNoticia, AgregarArticulo, EditarArticulo, BorrarArticulo, AgregarCategoria




urlpatterns = [
    path('index', views.index, name='index'),
    path('', PaginaPrincipal.as_view(), name='indexprueba'),
    path('noticia/<int:pk>/', DetalleNoticia.as_view(), name='pagina_noticia'),
    path('noticia/editar/<int:pk>/', EditarArticulo.as_view(), name='editararticulo'),
    path('contacto/', views.contacto, name='contacto'),
    path('suscripcion/', views.suscripcion, name='suscripcion'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('contacto-laboral/', views.contacto_laboral, name='contacto_laboral'),
    path('agregarnoticia/', AgregarArticulo.as_view(), name='agregarnoticia'),
    path('noticia/<int:pk>borrarnoticia/', BorrarArticulo.as_view(), name='borrarnoticia'),
    path('agregarcategoria/', AgregarCategoria.as_view(), name='agregar_categoria'),
    
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)