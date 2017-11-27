from django.contrib import admin

# Register your models here.
from .models import Restaurant, OpeningHour

admin.site.register(Restaurant)
admin.site.register(OpeningHour)