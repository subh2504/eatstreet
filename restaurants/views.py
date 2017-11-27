from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Prefetch, Avg, F, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from menus.models import Review
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


class RestaurentCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = RestaurantCreateForm
    success_url = "/restaurant/"
    template_name = "restaurants/form.html"

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(RestaurentCreateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context=super(RestaurentCreateView,self).get_context_data(**kwargs)
        context['title']='Add Restaurant'
        return context



class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        #r=Restaurant.objects.filter(active=True).prefetch_related(Prefetch('item_set',to_attr='items'))

        r=Restaurant.objects.all().prefetch_related('item_set').all()
        i=[]
        for rest in r:
            print(rest)
            i.append(rest.item_set.annotate(avg_rating = Avg('review__rating'),total_rating=Count('review')))
        print(list(r),list(i))# i=[]
        # for item in r:
        #     print(item.items)
        #     i.append(item.items.all.annotate(avgrating=Avg('review__rating')))
        # #i=Restaurant.objects.filter(active=True).prefetch_related(Prefetch('item_set',to_attr='items'))
        # print(i)
        return zip(r,i)


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()
    template_name='restaurants/restaurant_detail.html'
    # def get_queryset(self):
    #
    #     print(queryset)
    #     return queryset

    def get_context_data(self, **kwargs):

        context = super(RestaurantDetailView,self).get_context_data(**kwargs)
        #print(context['object'][0])

        context['restaurant'] = context['object'][1]
        context['object'] = context['object'][0]
        return context

    def get_object(self, queryset=None):
        obj = super(RestaurantDetailView, self).get_object(queryset=queryset)
        obj1=obj.item_set.annotate(avg_rating = Avg('review__rating'),total_rating=Count('review'))
        #print(obj)
        #print(obj1)
        return [list(obj1),obj]






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