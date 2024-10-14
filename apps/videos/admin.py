from django.contrib import admin
from .models import TopImageV, Video

@admin.register(TopImageV)
class TopImageVAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('description', 'type', 'videoUrl')