from django.conf.urls import url


from restaurants.views import home, about, contact, restaurant_listview, RestaurantListView, RestaurantDetailView,RestaurentCreateView

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(),name='list'),
    url(r'^create/$', RestaurentCreateView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='detail'),
]