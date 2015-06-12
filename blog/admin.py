from django.contrib import admin

# Register your models here.
from blog.models import Entrada, Categoria

admin.site.register(Entrada)
admin.site.register(Categoria)
