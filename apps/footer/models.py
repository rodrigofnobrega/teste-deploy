from django.db import models

class Contact(models.Model):
    phoneNumber = models.CharField(max_length = 15, verbose_name = 'Número do telefone')
    email = models.EmailField('Email')
    address = models.CharField(max_length = 255, verbose_name = 'Endereço')
    instagram = models.URLField(max_length = 255, verbose_name = 'Instagram')
    facebook = models.URLField(max_length = 255, verbose_name ='Facebook')
    youtube = models.URLField(max_length = 255, verbose_name = 'Youtube')
    
    def __str__(self):
        return f'{self.phoneNumber} - {self.email}'
    
class Information(models.Model):
    information_name = models.CharField(max_length = 30, verbose_name = 'Nome Site')
    information_url = models.URLField(max_length = 255, verbose_name ='URL Site')
    
    def __str__(self):
        return f'{self.information_name} - {self.information_url}'
