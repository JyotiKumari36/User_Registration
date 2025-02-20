from django import forms
from app.models import *

class UserMF(forms.ModelForm):
    class Meta:
        model=User
        #fields='_all_'
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class ProfileMF(forms.ModelForm):
    class Meta:
        model=Profile
        #fields='_all_'
        fields=['address','profile_pic']