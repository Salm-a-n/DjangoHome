from django.urls import path,include
from students import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('<str:msg>/', views.student_list, name='list'),
]