from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save

from restaurants.utils import unique_slug_generator


class ActiveRestaurantManager(models.Manager):
    def get_queryset(self):
        return super(ActiveRestaurantManager, self).get_queryset().filter(active=True)


class Restaurant(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    type = models.CharField(max_length=1, choices=(
        ('V', 'Vegetarian'),
        ('N', 'Non-Vegetarian'),), default='V')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=True)
    #objects = ActiveRestaurantManager()

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


WEEKDAYS = [
    ('Mo', "Monday"),
    ('Tu', "Tuesday"),
    ('We', "Wednesday"),
    ('Th', "Thursday"),
    ('Fr', "Friday"),
    ('Sa', "Saturday"),
    ('Su', "Sunday"),
]


class OpeningHour(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    weekday = models.CharField(
        choices=WEEKDAYS, max_length=2
    )

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('restaurant', 'weekday',)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Saving...")
    print(instance.timestamp)
    print(instance)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     print("Saved")
#     print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, Restaurant)
# post_save.connect(rl_post_save_receiver,Restaurant)
