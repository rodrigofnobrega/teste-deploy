from django.contrib import admin
from .models import Tool, Team

@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'image')