from django.db import models
import json

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=255)
	video_id = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	thumbnail = models.URLField()

	def json(self):
		return json.dumps({
			'title' : self.title,
			'video_id':self.video_id,
			'description':self.description,
			'thumbnail':self.thumbnail
		})
