from django import forms


# class RestaurantCreateForm(forms.Form):
#     name = forms.CharField()
#     location = forms.CharField(required=False)
from restaurants.models import Restaurant


class RestaurantCreateForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=['name','location']
