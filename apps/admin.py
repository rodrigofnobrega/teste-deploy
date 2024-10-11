from django.contrib import admin
from .models import Contact, Information, Tools, Team, TopImageV, Videos, TopDesc, DrawingAndCardAndKnow, TopImageF, Post, Comment, PopularTopic

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phoneNumber', 'email', 'address')

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('whoAreWe', 'randomUrl1', 'randomUrl2', 'randomUrl3')

@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')

@admin.register(TopImageV)
class TopImageVAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'tip', 'videoUrl')

@admin.register(TopDesc)
class TopDescAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(DrawingAndCardAndKnow)
class DrawingAndCardAndKnowAdmin(admin.ModelAdmin):
    list_display = ('tip', 'description')

@admin.register(TopImageF)
class TopImageFAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'userName', 'date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('userNameComment', 'post', 'date')

@admin.register(PopularTopic)
class PopularTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantityComments', 'date')
   