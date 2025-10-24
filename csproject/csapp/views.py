from django.shortcuts import render,redirect
from .forms import RegModelForm
from .models import Customer

def home(request):
    if request.method == 'POST':
        form=RegModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_customer')
        else:
            return render(request, 'registerform.html', {'form': form})
    else:
        form=RegModelForm()
        return render(request,'registerform.html',{'form':form})
def all_customer(request):
    all_cust=Customer.objects.all().order_by('name')
    return render(request,'allcustomer.html',{'all_cust':all_cust})
def filter(request):
    filt_cust=Customer.objects.filter(email__contains='@example.com').order_by('name')
    return render(request,'filter.html',{'filt_cust':filt_cust})
            
