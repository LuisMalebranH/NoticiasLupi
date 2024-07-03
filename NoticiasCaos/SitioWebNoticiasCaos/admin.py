from django.contrib import admin
from .models import Articulo, Categoria, Editor, Autor





# Register your models here.


admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Editor)