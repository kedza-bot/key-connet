from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from keyConnectapp.forms import LoginForm

# Create your views here.
def login_view(request):
    form=LoginForm(request.POST or None)
    if request.method == 'POST':
        username = form
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'keyConnectapp/login.html', {"form": form})  # Replace 'login.html' with your actual login template

def home_view(request):
    return render(request, 'keyConnectapp/index.html')  # Replace 'home.html' with your actual home page template