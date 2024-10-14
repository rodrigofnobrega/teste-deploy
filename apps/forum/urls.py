from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'), 
    path('criar/', views.criar_post, name="criar_post")
]