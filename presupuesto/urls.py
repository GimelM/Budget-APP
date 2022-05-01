
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_proyecto, name='lista'),
    path('<slug:proyecto_slug>', views.detalle_proyecto, name='detalle'),
]
