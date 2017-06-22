from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = User.objects.first()
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)