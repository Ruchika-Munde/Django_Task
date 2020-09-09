from .models import Employee
from django import forms
# class EmployeeForm(forms.ModelForm):  # model form

#     class Meta:
#         model=Employee
#         #fields=['eno','ename','esal','eaddr','email']
#         fields='__all__'

class NewEmployeeForm(forms.Form):
    eno = forms.IntegerField()  # this condition is used for validation=false
    ename = forms.CharField()
    esal = forms.FloatField()
    eaddr = forms.CharField()
    email = forms.EmailField()