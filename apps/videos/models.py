from django.db import models
from .utils import getTypeChoices

class TopImageV(models.Model): #V de Videos
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.description}'
    
class Video(models.Model):
    type = models.CharField(max_length = 20, choices=getTypeChoices())
    videoUrl = models.URLField(max_length = 255, verbose_name='URL do Vídeo')
    description = models.CharField(max_length = 50, verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description} - {self.type}'
    
class Category(models.Model):
    type = models.CharField(max_length = 20, choices=getTypeChoices())
    description = models.CharField(max_length = 50, verbose_name = 'Descrição')

    def __str__(self):
        return f'{self.description} - {self.type}'
