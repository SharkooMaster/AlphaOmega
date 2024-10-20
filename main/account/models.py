from django.contrib.auth.forms import User
from django.db import models

# Create your models here.

from playlist.models import PlayList


class Account (models.Model):
    user             = models.ForeignKey(User,on_delete=models.CASCADE)
    home_screen_tags = models.TextField(default="")
    # the key the user adds to search on youtube
    api_key          = models.TextField(default="")

    watch_later = models.ForeignKey(PlayList,on_delete=models.CASCADE,null=True)

    def create_watch_later(self):
        if self.watch_later is None:
            watch_later = PlayList(title='Watch Later', owner=self)
            watch_later.save()
            self.watch_later = watch_later
            self.save()
