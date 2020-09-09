from Commentapp.models import Comment
from django import forms

# class Commentform(forms.ModelForm):
#     class Meta:
#         model=Comment
#         fields='__all__'
#         exclude=['commentforpost','commentbyuser']

class commentform(forms.Form):
    commentbox=forms.CharField()
    cfileupload=forms.FileField(required=False) 

    