from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics


# FOR CHARLES DEO


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# FOR HOME


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AttractionsHomeViewSet(viewsets.ModelViewSet):
    queryset = AttractionsHome.objects.all()
    serializer_class = AttractionsHomeSerializer


class HomeReviewViewSet(viewsets.ModelViewSet):
    queryset = HomeReview.objects.all()
    serializer_class = HomeReviewSerializer


class AttractionCultureViewSet(viewsets.ModelViewSet):
    queryset = AttractionCulture.objects.all()
    serializer_class = AttractionCultureSerializer


# FOR REGIONS


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class PopularRegionViewSet(viewsets.ModelViewSet):
    queryset = PopularRegion.objects.all()
    serializer_class = PopularRegionSerializer


class PopularReviewViewSet(viewsets.ModelViewSet):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer


class ToTryViewSet(viewsets.ModelViewSet):
    queryset = ToTry.objects.all()
    serializer_class = ToTrySerializer


# FOR GALLERY

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

# FOR CULTURE


class CultureViewSet(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class NationalClothesViewSet(viewsets.ModelViewSet):
    queryset = NationalClothes.objects.all()
    serializer_class = NationalClothesSerializer


class HandCraftsViewSet(viewsets.ModelViewSet):
    queryset = HandCrafts.objects.all()
    serializer_class = HandCraftsSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class NationalInstrumentsViewSet(viewsets.ModelViewSet):
    queryset = NationalInstruments.objects.all()
    serializer_class = NationalInstrumentsSerializer


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer


# FOR FIVE_CATEGORIES

# for places


class PlacesRegionViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
# FOR Hotels


class HotelsRegionViewSet(viewsets.ModelViewSet):
    queryset = HotelsRegion.objects.all()
    serializer_class = HotelsRegionSerializer


class HotelsReviewViewSet(viewsets.ModelViewSet):
    queryset = HotelsReview.objects.all()
    serializer_class = HotelsReviewSerializer


# for kitchen


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer


class KitchenReviewViewSet(viewsets.ModelViewSet):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewSerializer


# FOR event

#  7 categories


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer


class EventConcertViewSet(viewsets.ModelViewSet):
    queryset = EventConcert.objects.all()
    serializer_class = EventConcertSerializer


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class EventCinemaViewSet(viewsets.ModelViewSet):
    queryset = EventCinema.objects.all()
    serializer_class = EventCinemaSerializer


class LeisureViewSet(viewsets.ModelViewSet):
    queryset = Leisure.objects.all()
    serializer_class = LeisureSerializer


class EventLeisureViewSet(viewsets.ModelViewSet):
    queryset = EventLeisure.objects.all()
    serializer_class = EventLeisureSerializer


class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


class EventTheaterViewSet(viewsets.ModelViewSet):
    queryset = EventTheater.objects.all()
    serializer_class = EventTheaterSerializer


class MasterClassesViewSet(viewsets.ModelViewSet):
    queryset = MasterClasses.objects.all()
    serializer_class = MasterClassesSerializer


class EventMasterViewSet(viewsets.ModelViewSet):
    queryset = EventMaster.objects.all()
    serializer_class = EventMasterSerializer


class TourismViewSet(viewsets.ModelViewSet):
    queryset = Tourism.objects.all()
    serializer_class = TourismSerializer

#FOR Attractions


class AttractionsEventViewSet(viewsets.ModelViewSet):
    queryset = AttractionsEvent.objects.all()
    serializer_class = AttractionsEventSerializer


class AttractionsEventReviewViewSet(viewsets.ModelViewSet):
    queryset = AttractionsEventReview.objects.all()
    serializer_class = AttractionsEventReviewSerializer

# FOR FAVORITE


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
