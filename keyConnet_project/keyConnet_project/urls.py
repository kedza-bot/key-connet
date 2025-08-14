# keyConnet_project/urls.py

from django.contrib import admin
from django.urls import path
from keyConnectapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home / Static pages
    path('', views.home_view, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('base/', views.home_view, name='base'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Profile
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Blog
    path('blog/', views.blog_view, name='blog'),
    path('blog/new/', views.blog_create_view, name='create_blog'),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),

    # Community / Q&A
    path('community/', views.community_list, name='community_list'),
    path('community/ask/', views.ask_question, name='ask_question'),
    path('community/<int:question_id>/', views.question_detail, name='question_detail'),
]

# Serve static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
