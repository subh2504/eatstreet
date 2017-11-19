from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from restaurants.models import Restaurant


class Item(models.Model):
    #associations
    user=models.ForeignKey(User)
    restaurant=models.ForeignKey(Restaurant)
    #user stuff
    name=models.CharField(max_length=120)
    contents=models.TextField(help_text="Seprate each items by comma",blank=True,null=True)
    public=models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('menus:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering=['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")

    def __str__(self):
        return self.name