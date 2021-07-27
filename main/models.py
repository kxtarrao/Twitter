from django.db import models
from django.contrib.auth.models import User
import datetime


class Tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    tweet_text = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=datetime.datetime.utcnow)

    author = models.ForeignKey(User,on_delete=models.PROTECT)

    def __repr__(self):
        return f"Tweet {self.id}:{self.tweet_text}"
