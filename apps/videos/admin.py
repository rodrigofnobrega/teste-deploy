from django.contrib import admin
from django import forms
from .models import TopImageV, Video, Category, PageDescription, TopImageVideo1, TopImageVideo2, TopImageVideo3, TopImageVideo4, TopImageVideo5, TopImageVideo6, TopImageVideo7

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['description', 'type', 'videoUrl']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'})  # Exibe um dropdown de seleção
        }

@admin.register(TopImageVideo1)
class TopImageVideo1Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo2)
class TopImageVideo2Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo3)
class TopImageVideo3Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo4)
class TopImageVideo4Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo5)
class TopImageVideo5Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo6)
class TopImageVideo6Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageVideo7)
class TopImageVideo7Admin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(TopImageV)
class TopImageVAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('description', 'type', 'videoUrl')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')

@admin.register(PageDescription)
class PageDescription(admin.ModelAdmin):
    list_display = ('description',)