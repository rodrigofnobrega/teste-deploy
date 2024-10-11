from django.db import models

class TopDesc(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class DrawingAndCardAndKnow(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    file = models.FileField(upload_to = 'downloads/', blank=True, null=True, verbose_name = 'Arquivo para Download')
    type = models.CharField(max_length = 30, verbose_name = "Tipo")
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.type} - {self.description}'