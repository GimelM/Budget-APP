from django.contrib import admin
from .models import Presupuesto_Proyecto, Proyecto, Categoria

admin.site.register(Presupuesto_Proyecto)
admin.site.register(Proyecto)
admin.site.register(Categoria)