from rest_framework import serializers
from .models import *

# FOR CHARLES DEO


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'user_picture', 'from_user']


# FOR Attraction
class AttractionReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionReview
        fields = ['avg_rating', 'rating_count']


class AttractionsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttractionsImage
        fields = ['image']


class AttractionsListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    image = AttractionsImageSerializers(read_only=True, many=True)

    class Meta:
        model = Attractions
        fields = ['attraction_name', 'image', 'description', 'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class AttractionsDetailSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()
    image = AttractionsImageSerializers(read_only=True, many=True)

    class Meta:
        model = Attractions
        fields = ['attraction_name', 'image', 'description', 'rating_count']

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HomeSerializer(serializers.ModelSerializer):
    attractions_home = AttractionsListSerializer(read_only=True, many=True)

    class Meta:
        model = Home
        fields = ['home_name', 'home_image', 'home_description', 'attractions_home']


# FOR REGIONS


class PopularPlacesListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = PopularPlaces
        fields = ['popular_name', 'popular_image', 'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class ToTrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ToTry
        fields = ['to_name', 'description', 'images']


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['image']


class RegionSerializer(serializers.ModelSerializer):
    popular_places = PopularPlacesListSerializer(read_only=True, many=True)
    What_to_try = ToTrySerializer(read_only=True, many=True)

    class Meta:
        model = Region
        fields = ['region_name', 'region_image', 'region_description', 'What_to_try', 'popular_places']


class PopularReviewSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    static = serializers.SerializerMethodField()
    client = UserProfileSimpleSerializer(read_only=True)
    review_image = ReviewImageSerializer(read_only=True, many=True)

    class Meta:
        model = PopularReview
        fields = ['client', 'created_date', 'comment', 'static', 'avg_rating', 'rating_count', 'review_image']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()

    def get_static(self, obj):
        return obj.get_static()


class PopularPlacesDetailSerializer(serializers.ModelSerializer):
    popular_reviews = PopularReviewSerializer(read_only=True, many=True)

    class Meta:
        model = PopularPlaces
        fields = ['popular_name', 'popular_image', 'description', 'popular_reviews']

# FOR Hotels


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelsImage
        fields = ['image']


class HotelsListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    hotel_image = HotelImageSerializers(read_only=True, many=True)

    class Meta:
        model = Hotels
        fields = ['name', 'hotel_image', 'average_rating', 'rating_count']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(read_only=True, many=True)

    class Meta:
        model = Hotels
        fields = ['name', 'hotel_image', 'address', 'bedroom', 'bathroom', 'cars_bikes',
                  'pets', 'amenities', 'safety_hygiene', 'price_short_period',
                  'price_medium_period', 'price_long_period']


class HotelsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsReview
        fields = '__all__'


# For Kitchen
class KitchenImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = KitchenImage
        fields = ['image']


class KitchenListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    kitchen_image = KitchenImageSerializers()

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'price', 'type_of_cafe', 'average_rating', 'rating_count', 'kitchen_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class KitchenDetailSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    kitchen_image = KitchenImageSerializers()
    nutrition_rating = serializers.SerializerMethodField()
    service_rating = serializers.SerializerMethodField()
    price_rating = serializers.SerializerMethodField()
    atmosphere_rating = serializers.SerializerMethodField()

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'kitchen_image', 'price', 'specialized_menu', 'meal_time', 'description',
                  'average_rating', 'rating_count', 'nutrition_rating', 'service_rating', 'price_rating', 'atmosphere_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()

    def get_nutrition_rating(self, obj):
        return obj.get_nutrition_rating()

    def get_service_rating(self, obj):
        return obj.get_service_rating()

    def get_price_rating(self, obj):
        return obj.get_price_rating()

    def get_atmosphere_rating(self, obj):
        return obj.get_atmosphere_rating()


class KitchenReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenReview
        fields = '__all__'


class EventCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = EventCategories
        fields = ['category']


class EventSerializers(serializers.ModelSerializer):
    category = EventCategorySerializers(read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'image', 'category', 'date', 'time', 'address', 'price']


class CultureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = ['culture_name', 'culture_description', 'culture_image']


class GamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['games_name', 'games_description', 'games_image']


class NationalClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalClothes
        fields = ['clothes_name', 'clothes_description', 'clothes_image']


class HandCraftsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HandCrafts
        fields = ['hand_name', 'hand_description', 'hand_image']


class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_name', 'currency_description', 'hand_image']


class NationalInstrumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalInstruments
        fields = ['national_name', 'national_description', 'national_image']


class CultureKitchenSerializers(serializers.ModelSerializer):
    class Meta:
        model = CultureKitchen
        fields = ['kitchen_name', 'kitchen_description', 'kitchen_image']


class GallerySerializers(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['gallery_name', 'gallery_image', 'address', 'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()
