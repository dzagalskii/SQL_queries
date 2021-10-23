from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_queries, name='all_queries'),
]
