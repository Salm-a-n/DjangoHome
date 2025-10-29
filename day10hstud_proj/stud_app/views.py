from django.shortcuts import render, redirect
from .forms import std_form
from.models import Std_manage
def create_student(request):
    if request.method == 'POST':
        form = std_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =std_form()
    return render(request, 'stud_app/add.html', {'form': form})
def all_data (request):
    stud_list = Std_manage.objects.all()
    return render(request, 'stud_app/home.html', {'stud_list':stud_list})

def update_student(request, id):
    stud_list = Std_manage.objects.get(pk=id) 
    if request.method == 'POST':
        form = std_form(request.POST,instance=stud_list)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =std_form(instance=stud_list)           
    return render(request, 'stud_app/edit.html', {'form': form})
def delete_student(request,title):
    stud_list=Std_manage.objects.get(title=title)  
    if request.method == 'POST':
        stud_list.delete()
        return redirect('home')
    
    return render(request,'stud_app/delete.html',{'stud_list':stud_list})

