from django.shortcuts import render


# Create your views here.

from .models import Restaurant

def restaurant_listview(request):
    template_name='restaurants/restaurants_list.html'
    queryset=Restaurant.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,template_name,context)












def home(request):
    context={

    }
    return render(request, 'index.html',context)


def contact(request):
    context={

    }
    return render(request, 'contact.html',context)


def about(request):
    context={

    }
    return render(request, 'about.html',context)