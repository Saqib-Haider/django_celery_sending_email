from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('excel', views.simple_upload, name='uploadindatabase'),
]