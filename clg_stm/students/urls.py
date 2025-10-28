from django.urls import path,include
from students import views

urlpatterns = [
    path('<str:msg>/', views.student_list, name='list'),
]