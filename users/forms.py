from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Profile



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class Edit_Profile_Form(forms.ModelForm):
    class Meta:
        model=User_Profile
        fields=['user_name','user_image','user_location']