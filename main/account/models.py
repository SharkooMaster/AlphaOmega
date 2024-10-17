from django.contrib.auth.forms import User
from django.db import models

# Create your models here.

class Account (models.Model):
    user             = models.ForeignKey(User,on_delete=models.CASCADE)
    home_screen_tags = models.TextField(default="")
    # the key the user adds to search on youtube
    api_key          = models.TextField(default="")
