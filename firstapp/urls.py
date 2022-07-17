from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('teste' , views.likelihood_end , name='teste'),
    path('relevance_region', views.relevance_region , name= 'relevance_region'),
    path('relevance_pestle', views.relevance_pestle , name='relevance_pestle'),
]