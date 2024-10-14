from django.contrib import admin
from .models import TopDesc, Material, CategoryP

@admin.register(TopDesc)
class TopDescAdmin(admin.ModelAdmin):
    list_display = ('description',) 
    search_fields = ('description',)  
    
@admin.register(Material)
class Material(admin.ModelAdmin):
    list_display = ('description', 'type')  
    list_filter = ('type',)  
    search_fields = ('type', 'description',) 

@admin.register(CategoryP)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')  
    list_filter = ('type',) 
    search_fields = ('description',) 
