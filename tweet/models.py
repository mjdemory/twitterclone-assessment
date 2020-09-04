from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.


    
class TweetModel(models.Model):
    body = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body