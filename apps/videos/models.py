from django.db import models

class TopImageV(models.Model): #V de Videos
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Video(models.Model):
    TYPE_CHOICES = [
        ('educativo', 'Educativo'),
        ('tutorial', 'Tutorial'),
        ('dormir', 'Dormir'),
        ('interativo', 'Interativo'),
    ]
    type = models.CharField(max_length = 20, choices=TYPE_CHOICES)
    videoUrl = models.URLField(max_length = 255, verbose_name='URL do Vídeo')
    description = models.CharField(max_length = 50, verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description} - {self.type}'