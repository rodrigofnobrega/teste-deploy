from django.contrib import admin
from .models import TopImageF, Post, Comment, PopularTopic

@admin.register(TopImageF)
class TopImageFAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'userName', 'date', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('userNameComment', 'post', 'date', 'commentDesc')

@admin.register(PopularTopic)
class PopularTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantityComments', 'date', 'subject')