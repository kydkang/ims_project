from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):        # will be used in SignUp view class in the next chapter
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = ('username', 'email', )   # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', )   # new
