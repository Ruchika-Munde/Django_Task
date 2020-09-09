from Firstapp.models import Summaryimages
from django import forms

class Summaryform(forms.ModelForm):
    class Meta:
        model=Summaryimages
        fields='__all__'

