from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'input input-bordered input-primary w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600','placeholder':'Enter your email address'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input input-bordered input-primary w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600 ','placeholder':'Enter your Name'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'input input-bordered input-primary w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    password2 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input input-bordered input-primary w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    
    class Meta:
        model = User
        fields = {'email','username','password1','password2',}