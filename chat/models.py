from django.db import models
from datetime import datetime

# Create our models here.
class Room(models.Model):
  name = models.CharField(max_length=500)
class Message(models.Model):
  text = models.CharField(max_length=5000)
  date = models.DateTimeField(default=datetime.now(), blank=True)
  user = models.CharField(max_length=500)
  room = models.CharField(max_length=500)
