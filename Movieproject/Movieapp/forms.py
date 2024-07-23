from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=('title','description','image','category','languages','actors','year','link','rating')

class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2')

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MovieUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']  # Include only the fields you need

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False
            field.help_text = ''