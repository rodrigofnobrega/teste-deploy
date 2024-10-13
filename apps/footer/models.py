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
    randomUrl1 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    randomUrl2 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    randomUrl3 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    whoAreWe = models.URLField(max_length = 255, verbose_name = 'Quem somos')
    
    def __str__(self):
        return f'{self.whoAreWe} - {self.randomUrl1} - {self.randomUrl2} - {self.randomUrl3}'
