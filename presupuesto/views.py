from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from presupuesto.forms import ExpenseForm
from .models import Presupuesto_Proyecto, Proyecto, Categoria
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpenseForm
import json

def listar_proyecto(request):
    listar_proyecto = Proyecto.objects.all()
    context = {
        'listar_proyecto': listar_proyecto
    }
    return render(request, 'presupuesto/listar-proyecto.html', context)

def detalle_proyecto(request, proyecto_slug):
    proyecto = get_object_or_404(Proyecto, slug=proyecto_slug)
    
    if request.method == 'GET':
        lista_categoria = Categoria.objects.filter(proyecto=proyecto)
        lista_presupuesto = proyecto.presupuestos.all()
        
        context = {
            'proyecto': proyecto,
            'lista_presupuesto': lista_presupuesto,
            'lista_categoria': lista_categoria,
            }
        
        return render(request, 'presupuesto/detalle-proyecto.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            monto = form.cleaned_data['monto']
            categoria_nombre = form.cleaned_data['categoria']
            
            categoria = get_object_or_404(Categoria, proyecto=proyecto, nombre=categoria_nombre)
            
            Presupuesto_Proyecto.objects.create(
                proyecto=proyecto,
                titulo=titulo,
                monto=monto,
                categoria = categoria
            ).save()
            
    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = Presupuesto_Proyecto.objects.get(id=id)
        expense.delete()

        return HttpResponse('')
            
    return HttpResponseRedirect(proyecto_slug)

class CrearProyecto(CreateView):
    model = Proyecto
    template_name = 'presupuesto/crear-proyecto.html'
    fields = ('nombre', 'presupuesto')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.guardar()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Categoria.objects.create(
                proyecto=Proyecto.objects.get(id=self.object.id),
                nombre=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['nombre'])