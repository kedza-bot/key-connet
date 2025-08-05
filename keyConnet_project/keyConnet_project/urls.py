"""
URL configuration for keyConnet_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from keyConnectapp import views  # Import views from keyConnectapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Home view
    path('login/', views.login_view, name='login'),  # Login view
    path('logout/', views.logout, name='logout'),  # Logout view
    path('profile/<int:user_id>/', views.profile_view, name='profile'),  # Profile view
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),  # Edit profile view
    path('base/', views.home_view, name='base'),  # Base view
    path('register/', views.register_view, name='register'),  # Register view
    path('blog/', views.blog_view, name='Blog'),  # Blog view
    path("blog/<int:blog_id>/", views.blog_detail_view, name="blog_detail"), # Blog detail view
]
