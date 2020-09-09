from Firstapp.models import Vehicle
from django import forms

class VehicleReg(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['Brand','Model','Price','Average']