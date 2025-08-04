from django.db import models

# Create your models here.
class Login(models.Model):
    # Field to store the username
    username = models.CharField(max_length=150)
    # Field to store the email address
    email = models.EmailField(max_length=254, unique=True)
    # Field to store the password (should be hashed in production)
    password = models.CharField(max_length=128)
    # Field to store the date and time when the user last logged in
    last_login = models.DateTimeField(null=True, blank=True)
    # 

    def __str__(self):
        # String representation of the model
        return self.username