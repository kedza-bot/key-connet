# from django import forms

# from keyConnectapp.models import Login


# class LoginForm(forms.ModelForm):
#     username = forms.CharField(max_length=150, required=True, label='Username')
#     password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

#     class Meta:
#         model = Login
#         fields = ('username', 'password')
        
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get("username")
#         password = cleaned_data.get("password")

#         if not username or not password:
#             raise forms.ValidationError("Both fields are required.")
        
#         return cleaned_data

# class RegisterForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=30, required=True, label='First Name')
#     last_name = forms.CharField(max_length=30, required=True, label='Last Name')
#     username = forms.CharField(max_length=150, required=True, label='Username')
#     email = forms.EmailField(required=True, label='Email')
#     password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

#     class Meta:
#         model = Login  # Assuming you want to use the Login model for registration
#         fields = ('first_name', 'last_name', 'username', 'email', 'password')

# keyConnectapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "short_description", "image", "icon", "content")
