from django import forms
from django.db import models
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email',widget=forms.TextInput(attrs={'placeholder':'Enter Your Email Address','type':'email'}))
    username=forms.CharField(required=True,label='Username', widget=forms.TextInput(attrs={'placeholder':'Enter Your Username'}))
    password1=forms.CharField(required=True,label='Password',widget=forms.TextInput(attrs={'placeholder':'Enter Your Password','type':'password'}))
    password2=forms.CharField(required=True,label='Confirm Password',widget=forms.TextInput(attrs={'placeholder':'Confirm Your Password','type':'password'}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')
        
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
