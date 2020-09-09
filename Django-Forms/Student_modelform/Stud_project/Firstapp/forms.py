from .models import Student
from django import forms

# class StudForm(forms.ModelForm):
#
#     class Meta:
#         model=Student
#         fields='__all__'

class NewStudentForm(forms.Form):
    rollno=forms.IntegerField()
    name=forms.CharField()
    marks=forms.FloatField()
    addr=forms.CharField()