from django.contrib import admin
from .models import Contact, Information

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('phoneNumber', 'email', 'address', 'instagram', 'facebook', 'youtube')

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('information_name', 'information_url',)
