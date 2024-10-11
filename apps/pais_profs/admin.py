from django.contrib import admin
from .models import TopDesc, DrawingAndCardAndKnow

@admin.register(TopDesc)
class TopDescAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(DrawingAndCardAndKnow)
class DrawingAndCardAndKnowAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'image', 'file')