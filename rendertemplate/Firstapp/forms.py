from django import forms
from Firstapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    # def cleaned_name(self):
    #     name=self.cleaned_name.get('name')
    #     if name=='Hello':
    #         raise forms.ValidationError("This is invalid name")
    #         return name

    # def cleaned_email(self):
    #     email=self.cleaned_email.get('email')
    #     if email=='@edu':
    #         raise forms.ValidationError("This is invalid email")
    #         return email