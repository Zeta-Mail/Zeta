from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Email(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=64)
    sender = models.CharField(max_length=64)
    username = models.CharField(max_length=64, null=True)
    body = models.TextField()
    time = models.CharField(max_length=64, null=True)
    date = models.CharField(max_length=64, null=True)
    spam = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject}"