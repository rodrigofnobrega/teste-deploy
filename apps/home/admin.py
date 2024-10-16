from django.contrib import admin
from .models import TopDescH, Tool, Team, Button

@admin.register(TopDescH)
class TopDescHAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'image')
    
@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('urls',) 