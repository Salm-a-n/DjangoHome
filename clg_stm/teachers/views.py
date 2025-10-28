from django.shortcuts import render

def teacher_list(request, msg):
    teachers = ['lini', 'adars', 'shankar']
    return render(request, 'teachers/teachers_list.html', {
        'teachers': teachers,
        'message': msg
    })
