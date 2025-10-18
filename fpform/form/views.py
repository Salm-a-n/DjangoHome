from django.shortcuts import render
def out(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     colour=request.POST.get('colour')
     return render(request,'outputform.html',{
         'formData':request.POST,
         'name': name,
         'colour':colour,
     })
    return render(request,'inputform.html')
