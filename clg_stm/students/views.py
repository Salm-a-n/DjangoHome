from django.shortcuts import render

def student_list(request, msg):
    students = ['salman', 'ashik', 'Charlie']
    return render(request, 'students/student_list.html', {
        'students': students,
        'message': msg
    })
def home(request):
    return render(request,'students/home.html')
