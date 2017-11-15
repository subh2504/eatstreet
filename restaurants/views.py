from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from restaurants.forms import RestaurantCreateForm
from .models import Restaurant

def restaurant_listview(request):
    template_name='restaurants/restaurants_list.html'
    queryset=Restaurant.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,template_name,context)


def restaurant_createview(request):
    form=RestaurantCreateForm(request.POST or None)
    errors=None

    if form.is_valid():
        form.save()
        return  HttpResponseRedirect('/reataurant/')
    if form.errors:
        errors=form.errors
    template_name='restaurants/form.html'
    queryset=Restaurant.objects.all()
    context={
        "form":form,
        "errors":errors
    }
    return render(request,template_name,context)


class RestaurentCreateView(CreateView):
    form_class = RestaurantCreateForm
    success_url = "/restaurant/"
    template_name = "restaurants/form.html"



class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug:
            queryset=Restaurant.objects.filter(Q(category_iexact=slug)|Q(category_icontains=slug))
        else:
            queryset=Restaurant.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()

    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView,self).get_context_data(**kwargs)
    #     print(context)
    #     return context
    #
    # def get_object(self, *args,**kwargs):
    #     rest_id=self.kwargs.get('rest_id')
    #     obj=get_object_or_404(Restaurant,id=rest_id)
    #     return obj






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