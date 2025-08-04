from django import forms

from keyConnectapp.models import Login


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    class Meta:
        model = Login
        fields = ('username', 'password')
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Both fields are required.")
        
        return cleaned_data