from django.db import models

# Create your models here.

class Account (models.Model):
    home_screen_tags = models.TextField()
