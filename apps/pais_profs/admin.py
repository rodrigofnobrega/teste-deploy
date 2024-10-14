from django.contrib import admin
from .models import TopDesc, DrawingAndCardAndKnow, CategoryP

@admin.register(TopDesc)
class TopDescAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title', 'description')  
    
@admin.register(DrawingAndCardAndKnow)
class DrawingAndCardAndKnowAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')  
    list_filter = ('type',)  
    search_fields = ('type', 'description',) 

@admin.register(CategoryP)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')  
    list_filter = ('type',) 
    search_fields = ('description',) 
