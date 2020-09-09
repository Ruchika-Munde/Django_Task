from .models import Student
from django import forms
class StudentReg(forms.ModelForm):

    class Meta:
        model=Student
        fields=['sid','sname','marks','addr']