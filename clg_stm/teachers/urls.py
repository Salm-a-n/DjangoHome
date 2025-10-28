# teachers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:msg>/', views.teacher_list, name='tlist'),  
]