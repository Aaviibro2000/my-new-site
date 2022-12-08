from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'input input-bordered input-primary w-full max-w-xs','placeholder':'Enter your email address'}))
    username = forms.CharField(required=True,)
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'input input-bordered input-primary w-full max-w-xs'}))
    password2 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input input-bordered input-primary w-full max-w-xs'}))
    
    class Meta:
        model = User
        fields = {'email','username','password1','password2',}