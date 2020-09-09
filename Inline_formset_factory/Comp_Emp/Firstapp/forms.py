from .models import Company,Employee
from django import forms
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class CompForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'