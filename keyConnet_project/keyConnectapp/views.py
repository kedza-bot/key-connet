
# keyConnectapp/views.py
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Profile, Blog

from .forms import RegisterForm, LoginForm, BlogForm
from .models import Profile, Blog

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # password hashed automatically
            # Create a profile
            Profile.objects.create(user=user, display_name=user.username)
            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "keyConnectapp/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")
    else:
        form = LoginForm(request)
    return render(request, "keyConnectapp/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")

def home_view(request):
    profile = None
    user_blogs = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        user_blogs = Blog.objects.filter(author=request.user)[:6]  # show latest 6
    return render(request, "keyConnectapp/index.html", {
        "profile": profile,
        "user_blogs": user_blogs,
    })

@login_required
def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog posted!")
            return redirect("home")
    else:
        form = BlogForm()
    return render(request, "keyConnectapp/blog_create.html", {"form": form})

def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "keyConnectapp/blog_detail.html", {"blog": blog})

def profile_view(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)
    profile = Profile.objects.filter(user=user_obj).first()
    blogs = getattr(user_obj, "blogs", None)
    blogs = blogs.all()[:6] if blogs else []  # latest 6 if Blog.related_name="blogs"
    ctx = {
        "profile_user": user_obj,
        "profile": profile,
        "blogs": blogs,
    }
    return render(request, "keyConnectapp/profile.html", ctx)

def blog_view(request):
    return render(request, 'keyConnectapp/blog.html')  # Adjust this to your template

