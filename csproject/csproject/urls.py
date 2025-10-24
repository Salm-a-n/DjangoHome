from django.contrib import admin
from django.urls import path
from csapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('all/',views.all_customer,name='all_customer'),
    path('filter/',views.filter,name='filter'),
    ]
