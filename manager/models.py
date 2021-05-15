from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True


class PasswordRecord(models.Model):
    email = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='email')
    name = models.CharField(max_length=200)
    website = models.URLField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.email, self.name)
