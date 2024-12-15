from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'


class CountryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryFood
        fields = '__all__'


class PopularPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlaces
        fields = '__all__'


class PopularReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularReview
        fields = '__all__'
