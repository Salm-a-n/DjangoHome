from django.urls import path
from . import views

urlpatterns = [
    path('<str:msg>/', views.student_list, name='list'),
]