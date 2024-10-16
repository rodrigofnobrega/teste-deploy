from django.contrib import admin
from django import forms
from .models import TopImageV, Video, Category

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['description', 'type', 'videoUrl']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'})  # Exibe um dropdown de seleção
        }

@admin.register(TopImageV)
class TopImageVAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('description', 'type', 'videoUrl')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')