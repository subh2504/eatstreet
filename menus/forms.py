from django import forms


# class RestaurantCreateForm(forms.Form):
#     name = forms.CharField()
#     location = forms.CharField(required=False)
from menus.models import Item
from restaurants.models import Restaurant


class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=[
            'restaurant',
            'name',
            'contents',
            'public'
        ]
    def __init__(self,user=None,*args,**kwargs):
        super(ItemForm,self).__init__(*args,**kwargs)
        self.fields['restaurant'].queryset=Restaurant.objects.filter(owner=user)