from django.db import models

# Create your models here.
from django.db.models.signals import pre_save,post_save

from restaurants.utils import unique_slug_generator


class Restaurant(models.Model):
    name=models.CharField(max_length=120)
    location=models.CharField(max_length=120,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name



def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    print("Saving...")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
        instance.save()

# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     print("Saved")
#     print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver,Restaurant)
#post_save.connect(rl_post_save_receiver,Restaurant)