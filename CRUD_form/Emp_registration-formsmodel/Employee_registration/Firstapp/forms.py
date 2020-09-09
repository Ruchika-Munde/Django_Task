from .models import Employee
from django import forms

class Empreg(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['eid','ename','designation','salary']