from django.db import models
from tweet.models import TweetModel
from twitteruser.models import TwitterUser

# Create your models here.
class Notification(models.Model):
     receiver = models.ForeignKey(TwitterUser, related_name="receiver", on_delete=models.CASCADE, blank=True, null=True)
     msg_content = models.ForeignKey(TweetModel, on_delete=models.CASCADE, blank=True, null=True)
     notification_flag = models.BooleanField(default=False)
