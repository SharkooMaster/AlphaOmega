from django.db import models

# Create your models here.

from page.models import Video

class PlayList(models.Model):

    title  = models.TextField(default="")
    videos = models.ManyToManyField(Video,related_name="playlists")

    owner = models.ForeignKey("account.Account", on_delete=models.CASCADE,related_name="playlists",null=True)
