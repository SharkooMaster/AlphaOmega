from django.db import models

# Create your models here.

class Channel (models.Model):
    channel_id = models.TextField()
    title = models.TextField()

    description = models.TextField(default="")

    subscriber_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    profile_high = models.URLField(default="")
    profile_medium = models.URLField(default="")
    profile_small = models.URLField(default="")
