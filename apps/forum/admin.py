from django.contrib import admin
from .models import TopImage, Post, Comment, PopularTopic, PageDescription

@admin.register(TopImage)
class TopImageFAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'pos')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'userName', 'date', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('userNameComment', 'post', 'date', 'commentDesc')

@admin.register(PopularTopic)
class PopularTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantityComments', 'date', 'subject')

@admin.register(PageDescription)
class PageDescription(admin.ModelAdmin):
    list_display = ('description',)