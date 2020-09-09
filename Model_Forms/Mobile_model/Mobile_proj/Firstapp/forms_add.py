from Firstapp.models import Mobile
from django import forms

class MobileReg(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=['Mname','Brand','Price','Ram']