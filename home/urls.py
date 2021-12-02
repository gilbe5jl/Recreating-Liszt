from django.urls import path
from . import views

#and then add path here to add new page

urlpatterns = [
    path('', views.home, name='home-home'),
    path('about/', views.about, name='home-about'),
    path('machine-learning/', views.AI, name='home-AI'),
    path('liszt/', views.liszt, name='home-liszt'),
    path('project/', views.project, name='home-project'),
    path('music/', views.music, name='home-music'),



]
    
