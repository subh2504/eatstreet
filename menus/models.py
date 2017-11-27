from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from restaurants.models import Restaurant


class Category(models.Model):
    name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=500, blank=True, null=True)
    type_of_dish = models.CharField(max_length=50, blank=True, null=True)
    place_of_origin = models.CharField(max_length=200, blank=True, null=True)
    main_ingredient = models.CharField(max_length=200, blank=True, null=True)
    region_or_state = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=500, blank=True, null=True)

    def get_other_name(self):
        return self.other_name.split(",")

    def get_place_of_origin(self):
        return self.place_of_origin.split(",")

    def get_main_ingredient(self):
        return self.main_ingredient.split(",")

    def get_region_or_state(self):
        return self.region_or_state.split(",")

    def __str__(self):
        return self.name


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, blank=True, null=True)
    type = models.CharField(max_length=1, choices=(
        ('V', 'Veg'),
        ('N', 'Non-Veg'),), default='V')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.name


class ActiveReviewManager(models.Manager):
    def get_queryset(self):
        return super(ActiveReviewManager, self).get_queryset().filter(public=True)


class Review(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    rating = models.FloatField(max_length=1, default=0, choices=(
        (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)))
    review = models.CharField(max_length=500, blank=True, null=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #objects = ActiveReviewManager()

    class Meta:
        ordering = ['-updated', '-timestamp']
        unique_together = ('user', 'item',)

    def __str__(self):
        return str(self.user) +" "+ str(self.item) +" "+str(self.rating)