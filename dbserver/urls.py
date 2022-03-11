from django.urls import path

from . import views

urlpatterns = [
    path('init_db', views.index, name='index'),
]
