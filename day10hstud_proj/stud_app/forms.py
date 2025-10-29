from django import forms
from .models import Std_manage

class std_form(forms.ModelForm):
    class Meta:
        model=Std_manage
        fields=['name','standard','age']