# keyConnectapp/views.py

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F

from .models import Profile, Blog, Question, Comment
from .forms import RegisterForm, BlogForm, ProfileForm, QuestionForm, CommentForm

# ==========================
# Auth & User Management
# ==========================

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            personal_details = form.cleaned_data.get("personal_details", "")

            # Create linked profile
            Profile.objects.create(
                user=user,
                display_name=user.username,
                bio=personal_details
            )

            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect("home")
        else:
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


# ==========================
# Home & Static Pages
# ==========================

def home_view(request):
    profile = Profile.objects.filter(user=request.user).first() if request.user.is_authenticated else None
    top_blogs = Blog.objects.all().order_by('-views')[:6]
    return render(request, "keyConnectapp/index.html", {
        "profile": profile,
        "top_blogs": top_blogs,
    })


def about_us(request):
    return render(request, "keyConnectapp/about_us.html")


# ==========================
# Blog Views
# ==========================

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
    Blog.objects.filter(id=blog_id).update(views=F('views') + 1)
    blog.refresh_from_db()
    return render(request, "keyConnectapp/blog_detail.html", {"blog": blog})


def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'keyConnectapp/blog.html', {'blogs': blogs})


# ==========================
# Profile Views
# ==========================

def profile_view(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)
    profile = Profile.objects.filter(user=user_obj).first()
    blogs = getattr(user_obj, "blogs", None)
    blogs = blogs.all()[:6] if blogs else []
    return render(request, "keyConnectapp/profile.html", {
        "profile_user": user_obj,
        "profile": profile,
        "blogs": blogs,
    })


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


# ==========================
# Community / Q&A Views
# ==========================

def community_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'keyConnectapp/community_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comments = question.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.question = question
                comment.save()
                return redirect('question_detail', question_id=question.id)
        else:
            return redirect('login')
    else:
        comment_form = CommentForm()

    return render(request, 'keyConnectapp/question_detail.html', {
        'question': question,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('community_list')
    else:
        form = QuestionForm()

    return render(request, 'keyConnectapp/ask_question.html', {'form': form})
