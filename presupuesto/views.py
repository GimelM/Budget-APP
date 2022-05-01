from django.shortcuts import render

def listar_proyecto(request):
    return render(request, 'presupuesto/listar-proyecto.html')

def detalle_proyecto(request, proyecto_slug):
    return render(request, 'presupuesto/detalle-proyecto.html')