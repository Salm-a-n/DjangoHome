from django import forms
from .models import Customer
class RegModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']