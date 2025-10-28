from django.shortcuts import render

def teacher_list(request, msg):
    teachers = ['Prof. Smith', 'Dr. Jane', 'Mr. Lee']
    return render(request, 'teachers/teacher_list.html', {
        'teachers': teachers,
        'message': msg
    })
