from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Proyecto, Categoria
from django.views.generic import CreateView
from django.utils.text import slugify

def listar_proyecto(request):
    return render(request, 'presupuesto/listar-proyecto.html')

def detalle_proyecto(request, proyecto_slug):
    proyecto = get_object_or_404(Proyecto, slug=proyecto_slug)
    lista_presupuesto = proyecto.presupuestos.all()
    context = {
        'proyecto': proyecto,
        'lista_presupuesto': lista_presupuesto
    }
    return render(request, 'presupuesto/detalle-proyecto.html', context)

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