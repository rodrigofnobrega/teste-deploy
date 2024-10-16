from django.db import models
from .utils import getTypeChoices

class TopImageVideo1(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo1.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo1, self).save(*args, **kwargs)
    
class TopImageVideo2(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo2.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo2, self).save(*args, **kwargs)
    
class TopImageVideo3(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo3.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo3, self).save(*args, **kwargs)

class TopImageVideo4(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo4.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo4, self).save(*args, **kwargs)
    
class TopImageVideo5(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo5.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo5, self).save(*args, **kwargs)
    
class TopImageVideo6(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo6.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo6, self).save(*args, **kwargs)
    
class TopImageVideo7(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    

    def save(self, *args, **kwargs):
        if TopImageVideo7.objects.exists() and not self.pk:
            raise ValueError("Apenas uma imagem é permitida.")
        super(TopImageVideo7, self).save(*args, **kwargs)

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
    
class PageDescription(models.Model):
    description = models.CharField(max_length = 50, verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description}'
