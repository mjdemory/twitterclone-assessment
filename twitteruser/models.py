from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class TwitterUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    # bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username