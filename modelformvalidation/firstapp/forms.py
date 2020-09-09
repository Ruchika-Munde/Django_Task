from django.forms import ModelForm
from django import forms
from firstapp.models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text","phone_number"]
    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()
        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')
        phone_number = self.cleaned_data.get('phone_number')
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post Should Contain minimum 10 characters'])
        if len(str(phone_number))!=10:
            self._errors['phone_number'] = self.error_class([
                'Phone_number Should Contain max 10 numbers'])
        # return any errors if found
        return self.cleaned_data
