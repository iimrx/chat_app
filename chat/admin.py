from django.contrib import admin
from .models import Room, Message

# Register our models here.
admin.site.register(Room)
admin.site.register(Message)