from django.db import models
from django.conf import settings

# models.py
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True)
    personal_details = models.TextField(blank=True)  # ✅ New field

    def __str__(self):
        return self.user.username



from django.db import models
from django.conf import settings

class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blogs"
    )
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    icon = models.ImageField(upload_to="blog_icons/", blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    is_top = models.BooleanField(default=False)# Tracks number of views

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} by {self.author.username}"
