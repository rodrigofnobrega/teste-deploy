from django.db import models
from .utils import getTypeChoices

class TopDesc(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description}'
    
class DrawingAndCardAndKnow(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    file = models.FileField(upload_to = 'downloads/', blank=True, null=True, verbose_name = 'Arquivo para Download')
    type = models.CharField(max_length=20, choices=getTypeChoices())
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description} - {self.type}' 
    
class CategoryP(models.Model):
    type = models.CharField(max_length=20, choices=getTypeChoices())
    description = models.CharField(max_length=50, verbose_name='Descrição')
    
    def __str__(self):
        return f'{self.description} - {self.type}'