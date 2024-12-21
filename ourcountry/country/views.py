from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics


# FOR CHARLES DEO


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# FOR HOME


class HomeListAPIView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AttractionsListAPIView(generics.ListAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsListSerializer


class AttractionsDetailAPIView(generics.RetrieveAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDetailSerializer


class AttractionReviewViewSet(viewsets.ModelViewSet):
    queryset = AttractionReview.objects.all()
    serializer_class = AttractionReviewSerializer

# FOR REGIONS


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class PopularPlacesListAPI(generics.ListAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesListSerializer


class PopularPlacesDetailAPI(generics.RetrieveAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesDetailSerializer


class PopularReviewViewSet(viewsets.ModelViewSet):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer


class ToTryViewSet(viewsets.ModelViewSet):
    queryset = ToTry.objects.all()
    serializer_class = ToTrySerializer


class HotelsListAPIView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsListSerializer


class HotelsDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDetailSerializer


class HotelsReviewViewSet(viewsets.ModelViewSet):
    queryset = HotelsReview.objects.all()
    serializer_class = HotelsReviewSerializer


# for kitchen


class KitchenListView(generics.ListAPIView):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenListSerializer


class KitchenDetailView(generics.RetrieveAPIView):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenDetailSerializers


class KitchenReviewViewSet(viewsets.ModelViewSet):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewSerializer


class EventListAPiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

