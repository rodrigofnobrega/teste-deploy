from django.db import models

class Tool(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    title = models.CharField(max_length = 50, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.title} - {self.description} - {self.image}'
    
class Team(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    name = models.CharField(max_length = 25, verbose_name = 'Nome')
    profession = models.CharField(max_length = 150, verbose_name = 'Profissão')
    
    def __str__(self):
        return f'{self.name} - {self.profession} - {self.image}'
    
class TopDescH(models.Model):
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description}'
    
class Button(models.Model):
    urls = models.URLField(max_length=200, verbose_name='Saiba mais urls')

    def __str__(self):
        return f'{self.urls}'