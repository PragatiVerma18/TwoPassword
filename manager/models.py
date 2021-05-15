from django.contrib.auth.models import User
from django.db import models


class PasswordRecord(models.Model):
    email = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    website = models.URLField(unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website
