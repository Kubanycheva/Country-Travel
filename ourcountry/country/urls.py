from django.urls import path, include
from .views import *
from rest_framework import routers


# FOR CHARLES DEO
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomeListAPIView.as_view(), name='home'),
    path('region/', RegionListAPIView.as_view(), name='region'),
    path('attractions/', AttractionsListAPIView.as_view(), name='attractions'),
    path('attractions/<int:pk>/', AttractionsDetailAPIView.as_view(), name='attractions_detail'),

    path('popular_places/', PopularPlacesListAPI.as_view(), name='region_popular_places'),
    path('popular_places/<int:pk>/', PopularPlacesDetailAPI.as_view(), name='region_popular_places_detail'),
    path('hotels/', HotelsListAPIView.as_view(), name='hotels_list'),
    path('hotels/<int:pk>/', HotelsDetailAPIView.as_view(), name='hotel_detail'),
    path('kitchen/', KitchenListView.as_view(), name='kitchen_list'),
    path('kitchen/<int:pk>/', KitchenDetailView.as_view(), name='kitchen_detail'),
    path('event/', EventListAPiView.as_view(), name='event'),


]
