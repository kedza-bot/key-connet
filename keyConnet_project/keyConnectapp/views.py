# keyConnectapp/views.py

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from .models import Profile, Blog
from .forms import RegisterForm, BlogForm
from .models import Profile, Blog

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("✅ FORM IS VALID — creating user now...")  # Debug

            # Save User instance
            user = form.save()
            personal_details = form.cleaned_data.get("personal_details", "")

            # Create linked profile
            Profile.objects.create(
                user=user,
                display_name=user.username,
                bio=personal_details
            )

            # Auto login user after registration
            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect("home")

        else:
            # Debug output to console
            print("❌ FORM IS INVALID — errors below:")
            for field, errors in form.errors.items():
                print(f"   {field}: {', '.join(errors)}")
            messages.error(request, "Please correct the errors below.")

    else:
        form = RegisterForm()

    return render(request, "keyConnectapp/register.html", {"form": form})




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")
    else:
        form = AuthenticationForm(request)
    return render(request, "keyConnectapp/login.html", {"form": form})



def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")




def home_view(request):
    profile = None
    top_blogs = Blog.objects.all().order_by('-views')[:6]  # top 6 blogs by views

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    return render(request, "keyConnectapp/index.html", {
        "profile": profile,
        "top_blogs": top_blogs,
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
    # Increment views count
    Blog.objects.filter(id=blog_id).update(views=F('views') + 1)
    # Refresh blog instance to have updated views
    blog.refresh_from_db()
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
    blogs = Blog.objects.all()  # Get all blogs for everyone to see
    return render(request, 'keyConnectapp/blog.html', {'blogs': blogs})




#profile edit view


@login_required
def edit_profile_view(request):
    profile = getattr(request.user, 'profile', None)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'keyConnectapp/edit_profile.html', {'form': form})



def about_us(request):
    return render(request, "keyConnectapp/about_us.html")
