from Postapp.models import Post
from django import forms

class Addpostform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=['postbyuser']