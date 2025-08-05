from django.db import models
from django.conf import settings

# # Create your models here.
# class Login(models.Model):
#     # Field to store the username
#     username = models.CharField(max_length=150)
#     # Field to store the email address
#     email = models.EmailField(max_length=254, unique=True)
#     # Field to store the password (should be hashed in production)
#     password = models.CharField(max_length=128)
#     # Field to store the date and time when the user last logged in
#     last_login = models.DateTimeField(null=True, blank=True)
#     # 

#     def __str__(self):
#         # String representation of the model
#         return self.username
    
#     #register the model in the admin interface
# class Register(models.Model):
#     # Field to store the user's first name
#     first_name = models.CharField(max_length=30)
#     # Field to store the user's last name
#     last_name = models.CharField(max_length=30)
#     # Field to store the username
#     username = models.CharField(max_length=150)
#     # Field to store the email address
#     email = models.EmailField(max_length=254, unique=True)
#     # Field to store the password (should be hashed in production)
#     password = models.CharField(max_length=128)
    
#     # Field to store the date and time when the user registered
#     date_joined = models.DateTimeField(auto_now_add=True)
#     # 

#     def __str__(self):
#         # String representation of the model
#         return self.username
    
    
 # keyConnectapp/models.py



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    icon = models.ImageField(upload_to="blog_icons/", blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} by {self.author.username}"