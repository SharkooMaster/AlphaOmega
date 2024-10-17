from django.db import models

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=255)
	video_id = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	thumbnail = models.URLField()
