from pyexpat import model
from django.db import models
from django.utils.text import slugify

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True, blank=True)
    presupuesto= models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    def guardar(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Proyecto, self).save(*args, **kwargs)
        
class Categoria(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Presupuesto_Proyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='presupuestos')
    titulo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo