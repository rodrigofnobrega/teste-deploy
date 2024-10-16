from django.db import models
from .utils import getNameChoices, getPosTopImages

class TopImage(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    pos = models.CharField(max_length = 20, choices=getPosTopImages())
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.description}'
    
class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Título')
    userName = models.CharField(max_length = 100, verbose_name = 'Nome de Usuário')
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data')
    description = models.TextField(verbose_name = 'Descrição')

    def __str__(self):
        return f'{self.title} - {self.userName} - {self.description}'

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comentarios', on_delete = models.CASCADE)  # Relaciona o comentário ao post
    userNameComment = models.CharField(max_length = 100, verbose_name = 'Autor', choices=getNameChoices())  # Nome do autor do comentário
    commentDesc = models.TextField(verbose_name = 'Descrição') 
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data') 

    def __str__(self):
        return f'{self.userNameComment}: {self.commentDesc[:30]}'
    
class PopularTopic(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Título')
    subject = models.TextField(verbose_name = 'Descrição')
    quantityComments = models.IntegerField(default=0, verbose_name='Quantidade de Comentários')
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data')
    
    def __str__(self):
        return f'{self.title} - {self.subject} - {self.quantityComments} - {self.date}'
    
class PageDescription(models.Model):
    description = models.CharField(max_length = 50, verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.description}'