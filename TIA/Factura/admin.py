from django.contrib import admin
from .models import Producto, Cliente, Categoria, Fatura, Vendedor
# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Fatura)
admin.site.register(Vendedor)
admin.site.register(Categoria)

