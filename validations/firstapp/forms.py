from django import forms
from firstapp.models import Student

class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.FloatField()
    email=forms.EmailField()

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<5:
            raise forms.ValidationError("min no.of character should be 5")
        return name
        
    def clean_marks(self):
        marks = self.cleaned_data['marks']
        if marks < 40.0:
            raise forms.ValidationError('marks should be greater than 40')
        return marks

    def clean_email(self):
        email=self.cleaned_data['email']
        if '.edu' in email:
            raise forms.ValidationError('We do not accept educational email')
        return email

    # def clean_address(self):
    #     l=['ahmadnagar','nagpur','yavatmal','pune','mumbai']
    #     address=self.cleaned_data['address']
    #     if address not in l:
    #         raise forms.ValidationError('we do not accept other address')
    #     return address
