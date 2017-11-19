from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView

from menus.forms import ItemForm
from .models import Item


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin,CreateView):
    template_name = 'restaurants/form.html'
    form_class=ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(ItemCreateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context=super(ItemCreateView,self).get_context_data(**kwargs)
        context['title']='Add Item'
        return context

    def get_form_kwargs(self):
        kwargs=super(ItemCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


class ItemUpdateView(LoginRequiredMixin,UpdateView):
    form_class=ItemForm
    template_name = 'restaurants/form.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context=super(ItemUpdateView,self).get_context_data(**kwargs)
        context['title']='Update Items'
        return context
    def get_form_kwargs(self):
        kwargs=super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

