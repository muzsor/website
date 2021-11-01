from django.urls import path

from . import views

app_name = 'app3'

urlpatterns = [
    path('', views.ShowCache, name='index'),
]
