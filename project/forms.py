from django import forms
from.models import Posts,Categories
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class products(forms.ModelForm):
    class Meta:
        model=Posts
        fields='__all__'

class products(forms.ModelForm):
    class Meta:
        model=Categories
        fields='__all__'

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'formstyle'}),
            'email':forms.EmailInput(attrs={'class':'formstyle'}),
        }
        