from django.shortcuts import render
def show_student(request):
    mystudent=[
        {'name':'Salman', 'age': 21,'Passed': True},
        {'name':'Akash', 'age': 24,'Passed': False},
        {'name':'Alfariz', 'age': 21,'Passed': True},
        {'name':'Vishnu', 'age': 25,'Passed': True},
        {'name':'Amal', 'age': 22,'Passed': False},
        {'name':'Fidhaan', 'age': 23,'Passed': True},
    ]
    context={'my_student':mystudent}
    return render(request,'student.html',context)
# Create your views here.
