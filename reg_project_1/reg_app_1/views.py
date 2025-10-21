from django.shortcuts import render
from .forms import RegForm
def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            return render(request,'thankyou.html',{
                 'name': form['name'].value
             })
    else:
        form = RegForm()
    return render(request,'index.html',{'form':form})
# Create your views here.
