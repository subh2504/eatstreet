"""eatstreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from restaurants.views import home, about, contact, restaurant_listview, RestaurantListView, RestaurantDetailView,restaurant_createview,RestaurentCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^about/', about),
    url(r'^contact/', contact),
    url(r'^restaurant/$', RestaurantListView.as_view()),
    url(r'^restaurant/create/$', RestaurentCreateView.as_view()),
    url(r'^restaurant/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    #url(r'^restaurant/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    #url(r'^restaurant/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),


]
