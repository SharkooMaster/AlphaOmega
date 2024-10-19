from django.db import models
import json

from channel.models import Channel

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=255)
	video_id = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	thumbnail = models.URLField()

	channel = models.ForeignKey(Channel,on_delete=models.CASCADE,related_name="videos",null=True)

	def json(self):
		return json.dumps({
			'title' : self.title,
			'video_id':self.video_id,
			'description':self.description,
			'thumbnail':self.thumbnail,
			'channel_id':self.channel.channel_id if self.channel != None else 0,
			'channel_title':self.channel.title if self.channel != None else 0
		})
