from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_control_works, name='all_control_works'),
    path('<control_work_id>', views.control_work, name='control_work'),
]
