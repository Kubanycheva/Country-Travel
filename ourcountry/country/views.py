from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class UserProfileListApiView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HomeListApiView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class RegionListApiView(generics.ListAPIView):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


class CountryFoodListApiView(generics.ListAPIView):
    queryset = CountryFood.objects.all()
    serializer_class = CountryFoodSerializer


class PopularPlacesListApiView(generics.ListAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesSerializer


class PopularPlacesListApiView(generics.ListAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesSerializer


class PopularPlacesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer

