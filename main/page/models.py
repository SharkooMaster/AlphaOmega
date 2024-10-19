from django.db import models

from channel.models import Channel

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=255)
	video_id = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	thumbnail = models.URLField()

	channel = models.ForeignKey(Channel,on_delete=models.CASCADE,related_name="videos",null=True)
