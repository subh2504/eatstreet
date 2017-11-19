from django.conf.urls import url


from restaurants.views import home, about, contact, restaurant_listview, RestaurantListView, RestaurantDetailView,restaurant_createview,RestaurentCreateView

urlpatterns = [
    url(r'^$', RestaurantListView.as_view()),
    url(r'^create/$', RestaurentCreateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
]