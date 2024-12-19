from rest_framework import serializers
from .models import *

# FOR CHARLES DEO


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# FOR HOME


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['home_name', 'home_image', 'home_description']


class AttractionsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionsHome
        fields = []


class HomeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeReview
        fields = '__all__'


class AttractionCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionCulture
        fields = '__all__'


# FOR REGIONS


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class PopularRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularRegion
        fields = '__all__'


class PopularReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularReview
        fields = '__all__'


class ToTrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToTry
        fields = '__all__'


# FOR GALLERY


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryReview
        fields = '__all__'


# FOR CULTURE


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'


class NationalClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalClothes
        fields = '__all__'


class HandCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandCrafts
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class NationalInstrumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalInstruments
        fields = '__all__'


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'


# FOR FIVE_CATEGORIES

# for places


class PlacesRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacesRegion
        fields = '__all__'

# FOR Hotels


class HotelsRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsRegion
        fields = '__all__'


class HotelsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsReview
        fields = '__all__'

# for kitchen


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'


class KitchenReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenReview
        fields = '__all__'

# FOR event

#  7 categories


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'


class EventConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventConcert
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class EventCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCinema
        fields = '__all__'


class LeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leisure
        fields = '__all__'


class EventLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLeisure
        fields = '__all__'


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'


class EventTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTheater
        fields = '__all__'


class MasterClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClasses
        fields = '__all__'


class EventMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMaster
        fields = '__all__'


class TourismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourism
        fields = '__all__'

#FOR Attractions


class AttractionsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionsEvent
        fields = '__all__'


class AttractionsEventReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionsEventReview
        fields = '__all__'

# FOR FAVORITE


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'
