from django.contrib import admin

# Register your models here.
from menus.models import Item,Review,Category


admin.site.register(Item)
admin.site.register(Review)
admin.site.register(Category)
