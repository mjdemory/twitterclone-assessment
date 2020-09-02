from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class TweetAuthorModel(models.Model):
    name = models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class TweetModel(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TweetAuthorModel, on_delete=models.CASCADE)