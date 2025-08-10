from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    personal_details = forms.CharField(
        label="Personal Details",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us more about yourself'}),
        required=False
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "personal_details"]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "short_description", "content", "image", "icon"]



#profile edit form
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself'}),
        }
