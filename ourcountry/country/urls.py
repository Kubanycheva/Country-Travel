from django.urls import path, include
from .views import *


urlpatterns = [
    path('user/', UserProfileListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user_detail'),


    path('home/', HomeListApiView.as_view(), name='home_list'),

    path('region/', RegionListApiView.as_view(), name='region_list'),

    path('country_food/', CountryFoodListApiView.as_view(), name='food_list'),


    path('popular_places/', PopularPlacesListApiView.as_view(), name='popular_list'),
    path('popular_places/<int:pk>/', PopularPlacesRetrieveUpdateAPIView.as_view(), name='popular_detail'),


    path('user/', UserProfileListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user_detail'),

]