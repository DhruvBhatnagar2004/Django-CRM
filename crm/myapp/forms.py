from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import record

# registration
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password']
        
# login
class loginform(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
# createrecord
class createrecord(forms.ModelForm):
    class Meta:
        model=record
        fields=['name', 'email', 'phone', 'city']
        
# updaterecord        
class updaterecord(forms.ModelForm):
    class Meta:
        model=record
        fields=['name', 'email', 'phone', 'city']