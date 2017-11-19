from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from restaurants.models import Restaurant


class Item(models.Model):
    #associations
    user=models.ForeignKey(User)
    restaurant=models.ForeignKey(Restaurant)
    #user stuff
    name=models.CharField(max_length=120)
    contents=models.TextField(help_text="Seprate each items by comma")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering=['-updated', '-timestamp']