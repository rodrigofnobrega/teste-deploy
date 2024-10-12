from django.urls import path
from . import views

urlpatterns = [
    path('', views.pais_profs, name='pais_profs'),
]